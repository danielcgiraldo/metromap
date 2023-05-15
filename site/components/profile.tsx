import React from "react";
import { useUser } from "@auth0/nextjs-auth0/client";

export default function Profile() {
    const { user, error, isLoading } = useUser();

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>{error.message}</div>;

    return (
        <div
            style={{
                display: "flex",
                flexDirection: "row",
                alignItems: "center",
            }}
        >
            {user ? (
                <div id="login-div">
                    <img
                        src={user.picture}
                        alt={user.name}
                    />
                    <a href="/api/auth/logout">
                        <svg width="691" height="709" viewBox="0 0 691 709" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M14.9827 0H675.036C683.994 0 690.719 7.4688 690.719 15.6827V692.909C690.719 701.868 683.25 708.592 675.036 708.592H15.7294C6.77099 708.592 0.046773 701.123 0.046773 692.909L0.0519814 15.6827C-0.698019 7.46907 6.76953 0 14.9827 0ZM88.1548 309.867H359.195L281.544 221.012C272.586 210.559 280.049 194.876 293.492 194.876L369.648 194.881C374.127 194.881 378.606 197.121 381.596 200.11L507.778 344.217C513.008 350.191 513.008 359.149 507.778 365.124L381.59 508.484C378.606 512.218 374.122 513.713 369.643 513.713H293.481C280.044 513.713 272.575 497.286 281.533 487.577L359.195 399.473H88.1548V604.806C88.1548 613.765 95.6235 620.489 103.837 620.489L585.437 620.484C594.396 620.484 601.12 613.015 601.12 604.801L601.115 105.281C601.115 96.3227 593.646 89.5984 585.432 89.5984H103.832C94.8738 89.5984 88.1496 97.0672 88.1496 105.281L88.1548 309.867Z" fill="black"/>
</svg>

                    </a>
                </div>
            ) : (
                <a href="/api/auth/login" id="login-btn">
                    Ingresar
                </a>
            )}
        </div>
    );
}
export { Profile };
