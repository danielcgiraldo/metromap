import { useId } from "react";
import styles from "./features.module.css";

export function Component({ title, url, status }) {
    return (
        <a
            className={styles[status]}
            href={url}
            target="_blank"
        >
            <p>{title}</p>
            <p>
                {status == "O"
                    ? "Operativo"
                    : status == "U"
                    ? "En mantenimiento"
                    : status == "M"
                    ? "Incidente Crítico"
                    : "Interrupción Parcial"}
            </p>
        </a>
    );
}

/** @type {{ title: string, data: {title: string, url: string, status: "O" | "U" | "M" | "P" }[]}[]} */
/**
 * O: Operative
 * U: Under maintenance
 * M: Major Outage
 * P: Partial Outage
 */
const SERVICE_LIST = [
    { title: "Twitter", data: [{ title: "Updates", url: "https://twitter.com/metrodemedellin", status: "U" }] },
    { title: "Api", data: [{ title: "/status", url: "https://api.metromap.online/v1/status", status: "U" }, { title: "/status/[line]", url: "https://api.metromap.online/v1/status/A", status: "U" }] },
    { title: "Mapa", data: [{ title: "Embed", url: "https://embed.metromap.online/v1/map", status: "U" }] }
];

export default function Features() {
    const keyId = useId();

    return (
        <div>
            <p>
                Powered by{" "}
                <a
                    href="https://twitter.com/metrodemedellin"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    @metrodemedellin
                </a>
            </p>
            <div>
                {SERVICE_LIST.map(({ title, data }) => (
                    <div>
                        <h3>{title}</h3>
                        {data.map(({ title, url, status }) => (
                            <Component title={title} url={url} status={status} />
                        ))}
                    </div>
                ))}
            </div>
        </div>
    );
}
