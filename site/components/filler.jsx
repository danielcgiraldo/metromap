import { useUser } from '@auth0/nextjs-auth0/client';

export default function Filler() {
    const { user } = useUser();
    const userEmail = user?.email;
    const modal = document.getElementById("skeleton");

    fetch(`https://api.metromap.online/v1/user/get/${userEmail}`)
    .then(response => response.json())
    .then(data => {
        if (data.status == "ok"){
            secret_key = data.data['secret_key']
            public_key = data.data['public_key']
            modal.querySelector(".body").innerHTML = `
            <p>A continuación se muestran sus credenciales para acceder a la API:</p>
            <ul>
              <li><strong>Public Key:</strong> ${public_key}</li>
              <li><strong>Secret Key:</strong> ${secret_key}</li>
            </ul>
            <p>Asegúrese de guardar estas credenciales en un lugar seguro y no compartirlos con nadie.</p>
            `
        }
        else{
            alert("Al menos funcionó XD")
        }
    })
    .catch(error => console.error(error));
}