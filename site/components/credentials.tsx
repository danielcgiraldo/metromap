// Imports
import { useUser } from "@auth0/nextjs-auth0/client";
import { useRouter } from "next/router";
import Request from "./request";

export default function Credentials() {
    // Destructure the user, error, and isLoading variables from the useUser hook
    const { user, error, isLoading } = useUser();
    // Extract the user ID from the user object
    const userID = user?.sub.split("|")[1];
    // Get the router object from the useRouter hook
    const router = useRouter();
    if (isLoading)
        return (
            <div id="loading-div">
                <img
                    src="https://metromapmed.s3.amazonaws.com/assets/img/loading.gif"
                    alt="Cargando..."
                />
            </div>
        );
    // Render an error message if there is an error
    if (error) return <div>{error.message}</div>;
    if (user) {
        // Render the Request component with the userID prop
        return <Request userID={userID} />;
    } else {
        // Redirect the user to the login page
        router.push("/api/auth/login");
        // Return null while redirecting or a loading indicato
        return null; // or a loading indicator while redirecting
    }
}
