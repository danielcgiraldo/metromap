import React from "react";
import { useUser } from "@auth0/nextjs-auth0/client";
import { useRouter } from "next/router";

export default function Profile() {
    const { user, error, isLoading } = useUser();
    const router = useRouter();

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>{error.message}</div>;
    if (user) {
        return <p>Hola</p>;
    } else {
        router.push("/api/auth/login");
        return null; // or a loading indicator while redirecting
    }
}
