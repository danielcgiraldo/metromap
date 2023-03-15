# Deploying a Production ready Django app on AWS

This tutorial is heavily influenced by [deploy-django.md](https://gist.github.com/rmiyazaki6499/92a7dc283e160333defbae97447c5a83#previewing-the-django-app-project-locally),
but has been modified slightly and includes some clarifications in order to deploy the Django App in AWS according to metromap requirements.

By following this tutorial, you will be able to successfully deploy the metromap Django app, which includes:

- An AWS EC2 server configured as hosting
- SSL-certification with Certbot
- A custom domain name

## Table of Contents

- [Deploying a Production ready Django app on AWS](#deploying-a-production-ready-django-app-on-aws)
  - [Table of Contents](#table-of-contents)
  - [Project Layout](#project-layout)
  - [Creating an AWS Account](#creating-an-aws-account)
  - [Creating an AWS EC2 Instance](#creating-an-aws-ec2-instance)
    - [_EC2 Console_](#ec2-console)
    - [_AMI_](#ami)
    - [_Security Groups_](#security-groups)
    - [_Instance Details_](#instance-details)
    - [_Key Pairs_](#key-pairs)
  - [Accessing your EC2 Instance](#accessing-your-ec2-instance)
    - [_Elastic IP_](#elastic-ip)
    - [_Connecting to your EC2 Instance_](#connecting-to-your-ec2-instance)
  - [EC2 Environment Setup](#ec2-environment-setup)
  - [Installing Dependencies](#installing-dependencies)
    - [_Firewall Setup_](#firewall-setup)
    - [_Setting up the Project on the Remote Server_](#setting-up-the-project-on-the-remote-server)
    - [_Configuring Gunicorn_](#configuring-gunicorn)
    - [_Configuring NGINX_](#configuring-nginx)
  - [Setting up your Domain](#setting-up-your-domain)
    - [_Creating Domain records_](#creating-domain-records)
    - [_Configuring our Web Server_](#configuring-our-web-server)
  - [HTTPS](#https)
    - [_Installing Certbot_](#installing-certbot)
  - [Closing Thoughts](#closing-thoughts)

---

## Project Layout

Here is the project layout:

```bash
ppi_06
├── AWS_deploy.md
├── core/ (Api & Embed powered by Django)
├── daniel.pem
├── integrantes.py
├── LICENSE
├── ppi_06_info02.md
├── README.md
└── site/ (Documentation powered by Nextra)
```

---

## Creating an AWS Account

Why choose AWS?

- It offers a lot of free services for new accounts.
- Very popular among startups and even enterprises.
- If you do not have an account, check out this step by step guide by Amazon [here](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).

Before you provision a new server, it is best practice to make sure your account is as secure as possible by following the prompts on your Security Status checklist. This can be found under the IAM tab from your console's homepage.

![security_status](https://user-images.githubusercontent.com/41876764/86527279-47d5a180-be52-11ea-97e0-537b62a987b7.png)

---

## Creating an AWS EC2 Instance

Amazon's EC2 or Elastic Compute Cloud is one of the core products/services AWS provides and is the main building block for many of AWS's other services. It allows users to essentially rent virtual computers on which to run their own applications. You can learn more about EC2 [here](https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud).

Start out by going into the AWS Console and going to the EC2 tab. An easy way to get there is through the Services link at the top and search for EC2 in the prompt.

> We selected "US East (N. Virginia) us-east-1" as our region of choice because it is relatively closer to Colombia compared to other locations. Additionally, it is one of the primary locations in AWS, and thus offers access to almost all of their products.

---

### _EC2 Console_

You should see this screen (as of July 2020):

![ec2_console](https://user-images.githubusercontent.com/41876764/86527285-5a4fdb00-be52-11ea-9de2-8ad9dabfd9f3.png)

Go to the **Running Instances** link on the EC2 dashboard and click Launch Instance.

![ec2_running_instances](https://user-images.githubusercontent.com/41876764/86527322-c8949d80-be52-11ea-9bcb-83ab9a1c8ac6.png)

---

### _AMI_

In this step, AWS will prompt you to choose an AMI. AMI's are templates to configure new instances. For this tutorial, we will be using Ubuntu 18.04 64-bit (free tier).

![ec2_choose_ami](https://user-images.githubusercontent.com/41876764/86527338-dba76d80-be52-11ea-834b-f0576918cc40.png)

Next, select the **t2.micro** instance type.

![ec2_choose_instance_type](https://user-images.githubusercontent.com/41876764/86527344-eb26b680-be52-11ea-8636-3c49552b5872.png)

On the next screen, keep clicking next until you see the option to **Configure Security Group**.

---

### _Security Groups_

Security groups are virtual firewalls for your instances.

**Important:** _by default, there is an implicit deny on all ports meaning if you do not add rules, all incoming/outgoing traffic is blocked. Security groups are also stateful, which means setting inbound rules for a certain port will also affect the outbound rules for that port._

Set your Security Group settings with the following:

| Type         | Port Range | Source            | Description.                                |
| ------------ | :--------: | :---------------: | ------------------------------------------: |
| SSH          | 22         | Custom YOUR-IP  | Port for SSH'ing into your server          |
| HTTP         | 80         | Anywhere          | Port for HTTP requests to your web server  |
| HTTPS        | 443        | Anywhere          | Port for HTTPS requests to your web server |
| Custom TCP   | 8000       | Anywhere          | Port which Django will run                 |

---

### _Instance Details_

Click forward to **Review and Launch** to view all configurations of your Instance/AMI.
If the configurations look correct go ahead and hit **Launch**.

---

### _Key Pairs_

Once you launch the instance, AWS will prompt you to create a key pair. A key pair consists of a public key that AWS stores and a private key file that you store. Together they allow you to connect to your instance securely through asymmetrical encryption.

If this is the first time you are creating a key pair for your project, select **Create a new key pair** from the drop-down and add a name for the key pair.

_Be sure to store the key pair in a secure location. It is generated only once and AWS will not have access to it if you lose it. This is your only means to log into the EC2 instance via SSH._

![key_pair](https://user-images.githubusercontent.com/41876764/86527366-0bef0c00-be53-11ea-9f2c-570e3daa3105.png)

Once you have downloaded the **key pair** make sure to move the **.pem** file to the root directory of your project on your local computer. It is also recommended to not upload the .pem file to GitHub. To ensure that the file is not accidentally uploaded to the repository, you should add it to the .gitignore file.

![mern-app_root_w_pem](https://user-images.githubusercontent.com/41876764/86527373-17423780-be53-11ea-91fe-fa2a108cc937.png)

Next, check the checkbox acknowledging that you have access to the private key pair and click Launch Instances. This should take you to the Launch Status page.

---

## Accessing your EC2 Instance

Click on the Instances tab on your EC2 console.

![ec2_instance_first_initializing](https://user-images.githubusercontent.com/41876764/86527378-21643600-be53-11ea-8323-f92d50ed00a8.png)

The instance may take a couple of minutes to launch. Once it passes its' status checks, the instance state should show a green circle and a "running" state.

---

### _Elastic IP_

Before you can log into your EC2 instance, it is important to first generate an Elastic IP and associate it to your EC2 instance.

An Elastic IP is a dedicated IP address for your EC2 instance. Although the instance has a public IP address assigned upon creation, that IP address is dynamic and does not persist if you stop and start the instance. With an Elastic IP address, you can mask the failure of an instance by remapping the address to another instance in your account.

Therefore, by using an Elastic IP, you can have a dedicated IP to which users from the internet can access your instance. This will come in handy later when you assign a custom domain name and add SSL certification to the server.

_Note: If you are using the free tier, AWS will charge you if your Elastic IP is NOT associated with an AWS identity._

On the EC2 dashboard, look under the **Network & Security** tab and go to **Elastic IPs**:

![elastic_ips_link](https://user-images.githubusercontent.com/41876764/86527387-2e812500-be53-11ea-92c6-806ecc97ae2c.png)

It should take you here:

![elastic_ip_addresses](https://user-images.githubusercontent.com/41876764/86527390-393bba00-be53-11ea-8c83-4496e091e78c.png)

Click on **Allocate Elastic IP address**.

It should take you here:

![allocate_ip_address](https://user-images.githubusercontent.com/41876764/86527396-422c8b80-be53-11ea-83a2-8c8b49963bbf.png)

Select **Allocate**.

![elastic_ip_created](https://user-images.githubusercontent.com/41876764/86527403-4f497a80-be53-11ea-8649-d00eded3a2dc.png)

This should create an Elastic IP. The next step is to associate that Elastic IP to the instance.

With the Elastic IP checked on the left side:

- Go to Actions
- Click on **Associate Elastic IP address**
- Make sure your Resource type is Instance
- Search for your instance (if this is your first time, it should be the only one)
- Click **Associate**

To check if everything is done correctly, go to the Instances tab and in the instance details, you should see the Elastic IP.

---

### _Connecting to your EC2 Instance_

With the instance selected in the EC2 console, click Connect near the top. You will be prompted with directions on how to connect to your EC2 instance:

![connect_to_your_instance](https://user-images.githubusercontent.com/41876764/86527414-5b353c80-be53-11ea-975f-c2f53c3e7de8.png)

- Changing the .pem file's permission to read-only ensures nobody can modify your private key.

Now that we have our instance and have allocated an Elastic IP to it.
It is time to connect to our server!

If you have not already, go to the **Instances** link in the EC2 Dashboard.

With the instance highlighted, click on **Connect** on the top banner of the Instaces Dashboard.

It should give you a pop up with directions on how to connect to your EC2 instance.

![connect_to_your_instance](https://user-images.githubusercontent.com/41876764/86527414-5b353c80-be53-11ea-975f-c2f53c3e7de8.png)

Go back to your project root directory and make sure that your **.pem** file has the correct permissions.

Run the command:

```bash
    chmod 400 *.pem
```

Next run the command given to you in the example:

```bash
    ssh -i "<KEY-PAIR>.pem" ubuntu@<YOUR-IP-ADDRESS>.compute-1.amazonaws.com
```

The ssh should prompt you that the authenticity of host _instance_ can't be established and will show an ECDSA key fingerprint.
It will also ask you `Are you sure you want to continue connecting (yes/no)?`

Type `yes` and _Enter_.

This should take you into the EC2 Instance.
If not, try the `ssh` command again.

Congratulations you are inside your EC2 Instance!

---

## EC2 Environment Setup

Once you are logged into your server, we will install all of the project dependencies:
We will install the following:

- Django and Python3
- pip
- gunicorn
- NGINX
- UFW (Firewall)

---

## Installing Dependencies

Updating packages:

```bash
% sudo apt update
% sudo apt upgrade
```

Installing Python 3, NGINX and Gunicorn:

```bash
% sudo apt install python3-pip python3-dev nginx gunicorn curl
```

---

### _Firewall Setup_

Enable Firewall and allow OpenSSH:

```bash
% sudo ufw enable
% sudo ufw allow OpenSSH
% sudo ufw allow 'Nginx Full'
```

Check to make sure we are allowing OpenSSH

```bash
% sudo ufw status
```

Expected output:

```bash
To                         Action      From
--                         ------      ----
Nginx Full                 ALLOW       Anywhere
OpenSSH                    ALLOW       Anywhere
Nginx Full (v6)            ALLOW       Anywhere (v6)
OpenSSH (v6)               ALLOW       Anywhere (v6)
```

---

### _Setting up the Project on the Remote Server_

To deploy our GitHub repository on our EC2 instance:

```bash
% git clone https://github.com/danielcgiraldo/ppi_06.git
% cd ppi_06/core
% python3 -m venv env
% source env/bin/activate
% pip3 install -r requirements.txt
```

**Note: Make sure to update your .env file so that your project has the correct Environment Varialbes necessary to run.**

---

### _Configuring Gunicorn_

Create a gunicorn.socket file:

```bash
% sudo vim /etc/systemd/system/gunicorn.socket
```

Configure the gunicorn.socket file with:

```bash
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Next configure the gunicorn.service file with:

```bash
% sudo nano /etc/systemd/system/gunicorn.service
```

Use the configurations below:

```bash
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=djangoadmin
Group=www-data
WorkingDirectory=/home/ubuntu/ppi_06/core
ExecStart=/home/djangoadmin/pyapps/venv/bin/gunicorn \
--access-logfile - --workers 3 --bind unix:/run/gunicorn.sock metromap.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start and enable Gunicorn:

```bash
% sudo systemctl start gunicorn
% sudo systemctl enable gunicorn
```

Check the status of gunicorn with:

```bash
% sudo systemctl status gunicorn
```

---

### _Configuring NGINX_

Next, we need to configure NGINX to redirect web traffic.

Create a new NGINX config file with the following command:

```bash
% sudo vim /etc/nginx/sites-available/metromap
```

Paste in the following configurations and replace any of the ALL CAPS sections with your own project details:

```bash
server {
listen 80;
server_name YOUR_INSTANCE_IP_ADDRESS;

location / {
include proxy_params;
proxy_pass http://unix:/run/gunicorn.sock;
}
}
```

Once your NGINX config is set up, make sure there are no syntax errors with:

```bash
% sudo nginx -t
```

Next, create a soft link of your config file from sites-available to the sites-enabled directory. This step is important because NGINX will use the configuration settings located at /etc/nginx/sites-available/default by default if there is nothing in sites-enabled.

```bash
% sudo ln -s /etc/nginx/sites-available/metromap /etc/nginx/sites-enabled
```

Restart the NGINX Web Server with:

```bash
% sudo systemctl restart nginx
```

Now if you go to your Elastic IP on your browser it should show the app!

[Back to Table of Contents](#table-of-contents)

---

## Setting up your Domain

So far, users can access the site using the Elastic IP. However, it can be difficult to remember and share so we will configure a custom domain name.

To get started, you need to first purchase a domain. This can range from $1 to $1,000+s. Amazon has a service called Route53 you can use or you can choose other providers such as [Google Domains](https://domains.google/), [GoDaddy](https://www.godaddy.com/), etc.

There are two steps you would need to configure to connect the project with a custom domain:

- Create domain records with DNS registrar
- Configure NGINX on the EC2 instance to recognize the domain

---

### _Creating Domain records_

Let's start with configuring our DNS with records:

- Go to the **DNS** portion of your registrar.
- Find where you can create custom resource records.

Set the records like so:

| Name | Type  | TTL | Data                    |
| ---- | :---: | :-: | ----------------------: |
| api    | A     | AUTO  | YOUR-ELASTIC-IP-ADDRESS |
| embed    | A     | AUTO  | YOUR-ELASTIC-IP-ADDRESS |

### _Configuring our Web Server_

Edit the NGINX config file inside your EC2 instance:

```bash
% sudo vim /etc/nginx/sites-available/default
```

Update the `server:server_name` section of the config file:

```bash
server {
server_name <YOUR-ELASTIC-IP> api.metromap.online embed.metromap.online;
...
```

Save and restart NGINX:

```bash
sudo sudo systemctl restart nginx
```

_DNS changes can take up to 48 hours to update so your results may vary. Once it is complete, going to your custom domain should redirect you to your app._

---

## HTTPS

Secure Sockets Layer (SSL) is a standard security technology for establishing an encrypted link between a server and a client. So far, we have been serving web content over HTTP, which can be dangerous as data sent between the server and client is not encrypted. If you are handling user sign-in and need to protect data such as passwords or credit card information, it is always best practice to have SSL certification on your applications.

In this tutorial, we will be using Certbot by letsencrypt.org, a non-profit organization that provides free SSL Certificates.

---

### _Installing Certbot_

On your browser go to <https://certbot.eff.org/instructions>.

Select the Software and Operating System (OS) you are using. In this case, we are using NGINX and Ubuntu 18.04 LTS (bionic).

Inside your EC2 Instance, follow the command-line instructions until you see these instructions:

```bash
% sudo certbot --nginx
```

After running this command, Certbot will present to you the following prompt: Which names would you like to activate HTTPS for?

If NGINX is configured correctly, it should show both your root domain as well as with the www subdomain:

```bash
1: api.metromap.online
2: embed.metromap.online
```

Select enter to activate both HTTP and HTTPs. The next prompt will be:

```bash
Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: No redirect - Make no further changes to the web server configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
```

Select option 2 as this will redirect all traffic through HTTPS and is the most secure option. Afterward, Certbot will make changes to the NGINX configuration file.

_Note: Once your site is using HTTPS, double-check your API calls and make sure that they are going to the <https://> endpoint rather than <http://>. This may be an unnecessary precaution, but it is an easy bug to miss._

Next, go to your custom domain. Check to see if there is a lock icon next to your URL.

![secure_site](https://user-images.githubusercontent.com/41876764/86527267-2674b580-be52-11ea-9405-874f4f4ba7f0.png)

Congratulations! You have successfully deployed a web app with HTTPS!

---

## Closing Thoughts

I hope this information was helpful for those who are new to web development and AWS. If you encounter any difficulties, please do not hesitate to contact either me or my colleagues for assistance.

We would like to express our gratitude to the author of [deploy-django.md](https://gist.github.com/rmiyazaki6499/92a7dc283e160333defbae97447c5a83), which was the main source of information used in this tutorial. We would also like to thank Chat GPT for assisting in improving the clarity of this document.

[Back to Table of Contents](#table-of-contents)
