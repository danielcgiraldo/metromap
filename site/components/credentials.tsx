import { useUser } from "@auth0/nextjs-auth0/client";
import { useRouter } from "next/router";
import Request from "./request";

export default function Credentials() {
    const { user, error, isLoading } = useUser();
    const userID = user?.sub.split("|")[1];
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
    if (error) return <div>{error.message}</div>;
    if (user) {
        return <Request userID={userID} />;
    } else {
        router.push("/api/auth/login");
        return null; // or a loading indicator while redirecting
    }
}
