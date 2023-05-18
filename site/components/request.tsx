"use client";

import React, { useState, useEffect } from "react";
export default function Request({ userID }: { userID: string }) {
    const [data, setData] = useState(null);
    const ref = React.useRef(null);
    const [domains, setDomains] = useState("");

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch(
                    `https://api.metromap.online/v1/user/get/${userID}`
                );
                const result = await res.json();
                setData(result);
                const domains = JSON.parse(result.data.allowed_domains);
                setDomains(domains.join(","));
            } catch (err) {
                console.error(err);
            }
        };
        fetchData();
    }, []);

    function validateDomains(domains) {
        var domainRegex = /^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,})$/;
        if (!domains.includes(",")) {
            domains = [domains];
        } else {
            domains = domains.split(",");
        }

        for (var i = 0; i < domains.length; i++) {
            var domain = domains[i].trim();

            if (!domainRegex.test(domain)) {
                return false;
            }
        }
        return domains;
    }

    useEffect(() => {
        const update_domains = async () => {
            try {
                const dom = validateDomains(domains);
                if (dom) {
                    const res = await fetch(
                        `https://api.metromap.online/v1/user/update/${userID}?allowed_domains=${JSON.stringify(
                            dom
                        )}`
                    );
                    const data = await res.json();
                    if (data.status === "ok") {
                        alert("Dominios actualizados correctamente");
                    } else {
                        alert("Error al actualizar los dominios");
                    }
                } else {
                    alert("Dominios no válidos");
                }
            } catch (error) {
                console.error(error);
            }
        };

        ref.current.addEventListener("click", update_domains);

        return () => {
            try {
                ref.current.removeEventListener("click", update_domains);
            } catch (error) {}
        };
    }, [ref, domains]);
    return (
        <div id="credenciales-div">
            <h1 className="nx-mt-2 nx-text-4xl nx-font-bold nx-tracking-tight nx-text-slate-900 dark:nx-text-slate-100">
                Credenciales
            </h1>
            <input
                type="text"
                disabled
                value={data ? "Créditos: " + data.data.credits : "Cargando..."}
            />
            <p className="nx-mt-6 nx-leading-7 first:nx-mt-0">
                Bienvenido a la página de credenciales de nuestro servicio. Aquí
                puede obtener las credenciales necesarias para integrar su
                aplicación con nuestros servicios. Es importante que proteja sus
                credenciales y las mantenga seguras en todo momento. Las
                credenciales son una parte fundamental de la autenticación de su
                aplicación y son la clave para acceder a nuestros servicios.
            </p>
            <h2 className="nx-font-semibold nx-tracking-tight nx-text-slate-900 dark:nx-text-slate-100 nx-mt-10 nx-border-b nx-pb-1 nx-text-3xl nx-border-neutral-200/70 contrast-more:nx-border-neutral-400 dark:nx-border-primary-100/10 contrast-more:dark:nx-border-neutral-400">
                Secret Key
            </h2>
            <p className="nx-mt-6 nx-leading-7 first:nx-mt-0">
                La clave secreta es un token de autenticación utilizado para
                autenticar sus solicitudes de API. Nunca comparta su clave
                secreta con terceros.
            </p>
            <input
                type="text"
                disabled
                value={data ? data.data.secret_key : "Cargando..."}
            />
            <h2 className="nx-font-semibold nx-tracking-tight nx-text-slate-900 dark:nx-text-slate-100 nx-mt-10 nx-border-b nx-pb-1 nx-text-3xl nx-border-neutral-200/70 contrast-more:nx-border-neutral-400 dark:nx-border-primary-100/10 contrast-more:dark:nx-border-neutral-400">
                Clave pública
            </h2>
            <p className="nx-mt-6 nx-leading-7 first:nx-mt-0">
                La clave pública se utiliza para validar las solicitudes de API
                que provienen de su dominio. Asegúrese de configurar los
                dominios permitidos correctamente para proteger su cuenta de
                acceso no autorizado.
            </p>
            <input
                type="text"
                disabled
                value={data ? data.data.public_key : "Cargando..."}
            />
            <h3 className="nx-font-semibold nx-tracking-tight nx-text-slate-900 dark:nx-text-slate-100 nx-mt-8 nx-text-2xl">
                Dominios Permitidos
            </h3>
            <p className="nx-mt-6 nx-leading-7 first:nx-mt-0">
                Los dominios permitidos son una lista de dominios aprobados para
                usar su clave pública. Asegúrese de separar los dominios por
                comas al agregarlos a la lista de dominios permitidos.
            </p>
            <div className="nextra-code-block nx-relative nx-mt-6 first:nx-mt-0">
                <pre className="nx-bg-primary-700/5 nx-mb-4 nx-overflow-x-auto nx-rounded-xl nx-font-medium nx-subpixel-antialiased dark:nx-bg-primary-300/10 nx-text-[.9em] contrast-more:nx-border contrast-more:nx-border-primary-900/20 contrast-more:nx-contrast-150 contrast-more:dark:nx-border-primary-100/40 nx-py-4 ">
                    Por ejemplo: dominio1.com,dominio2.com,dominio3.com
                </pre>
            </div>
            <p className="nx-mt-6 nx-leading-7 first:nx-mt-0">
                No debes incluir el protocolo (http:// o https://) en la lista,
                ni www. o cualquier subdominio. Solo incluya el nombre de
                dominio principal.
            </p>
            <input
                type="text"
                value={domains}
                disabled={data ? false : true}
                onChange={(e) => {
                    setDomains(e.target.value);
                }}
            />
            <p className="nx-mt-6 nx-leading-7 first:nx-mt-0">
                Recuerde que la seguridad es crucial cuando se trata de
                credenciales. Asegúrese de implementar todas las medidas de
                seguridad necesarias para proteger sus credenciales y evitar el
                acceso no autorizado.
            </p>
            <button ref={ref} className="btn default">
                Guardar
            </button>
        </div>
    );
}
