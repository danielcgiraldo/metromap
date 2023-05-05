import React from "react";
import { useAuth0, Auth0Provider } from "@auth0/auth0-react";

const LoginButton = () => {
  const { loginWithRedirect } = useAuth0();

  return <Auth0Provider
  domain="dev-bh0p6reo57zdtina.us.auth0.com"
  clientId="dQMJ2mQn5D7LAv0Ja04kjwt0KFWNxxyn"
  authorizationParams={{
    redirect_uri: "http://localhost:3000"
  }}
>
  <button onClick={() => loginWithRedirect()}>Log In</button> 
</Auth0Provider>
};

export default LoginButton;