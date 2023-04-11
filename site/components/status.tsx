import { useId } from "react";
import styles from "./status.module.css";

export function Component({ title, url, status, key, info = null }) {
    return (
        <a className={styles.status_row} href={url} key={key} target="_blank">
            <p className={styles.status_title}>
                {title}
                {info != null ? (
                    <div className={styles.tooltip}>
                        <svg
                            width="20"
                            height="20"
                            viewBox="0 0 1600 1600"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                d="M0 800C0 587.827 84.2867 384.347 234.307 234.307C384.333 84.28 587.827 0 800 0C1012.17 0 1215.65 84.2867 1365.68 234.307C1515.71 384.333 1600 587.827 1600 800C1600 1012.17 1515.71 1215.65 1365.68 1365.69C1215.65 1515.72 1012.17 1600 800 1600C587.827 1600 384.347 1515.71 234.307 1365.69C84.28 1215.67 0 1012.17 0 800ZM100 800C100 985.653 173.749 1163.69 305.027 1294.97C436.303 1426.25 614.347 1500 800 1500C985.653 1500 1163.69 1426.25 1294.97 1294.97C1426.25 1163.7 1500 985.653 1500 800C1500 614.347 1426.25 436.307 1294.97 305.027C1163.7 173.747 985.653 100 800 100C614.52 100.568 436.8 174.5 305.653 305.653C174.503 436.804 100.573 614.52 100 800ZM726.48 1250.75V1123.8H852.283V1250.75H726.48ZM727.756 1000.49C725.647 959.024 730.798 917.509 742.98 877.816C762.564 843.035 788.673 812.357 819.881 787.467C850.449 752.363 879.179 715.696 905.955 677.617C923.595 649.951 932.507 617.617 931.533 584.815C933.945 548.361 921.507 512.487 897.055 485.341C870.352 460.748 834.732 448.175 798.508 450.544C764.445 449.575 731.076 460.237 703.883 480.768C677.856 500.919 664.831 557.091 664.831 596.143H550.008L548.133 592.466C546.956 526.966 570.034 447.892 617.436 408.439H617.431C668.723 367.647 732.952 346.632 798.431 349.215C878.581 349.215 940.817 369.663 985.151 410.564H985.156C1007.87 432.663 1025.57 459.387 1037.05 488.928C1048.54 518.464 1053.53 550.126 1051.7 581.767C1052.07 633.002 1037.08 683.174 1008.68 725.82C975.722 774.404 937.536 819.222 894.801 859.474C876.681 875.52 862.916 895.895 854.801 918.698C849.218 945.583 846.858 973.036 847.78 1000.47L727.756 1000.49Z"
                                fill="#ADADAD"
                            />
                        </svg>
                        <span>{info}</span>
                    </div>
                ) : null}
            </p>
            <p className={styles[status]}>
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

/** @type {{ title: string, data: {title: string, url: string, status: "O" | "U" | "M" | "P", info: undefined | string }[]}[]} */
/**
 * O: Operative
 * U: Under maintenance
 * M: Major Outage
 * P: Partial Outage
 */
const SERVICE_LIST = [
    {
        title: "Twitter",
        data: [
            {
                title: "Updates",
                url: "https://twitter.com/metrodemedellin",
                status: "U",
                info: "Actualizar sistemas desde @metrodemedellin",
            },
        ],
    },
    {
        title: "Api",
        data: [
            {
                title: "/status",
                url: "https://api.metromap.online/v1/status",
                status: "U",
            },
            {
                title: "/status/:line",
                url: "https://api.metromap.online/v1/status/A",
                status: "U",
            },
            {
                title: "/status/:line/:station",
                url: "https://api.metromap.online/v1/status/A/san_antonio",
                status: "U",
            },
            {
                title: "/data",
                url: "https://api.metromap.online/v1/data",
                status: "U",
            },
            {
                title: "/data/:line",
                url: "https://api.metromap.online/v1/data/A",
                status: "U",
            },
            {
                title: "/data/:line/:station",
                url: "https://api.metromap.online/v1/data/A/san_antonio",
                status: "U",
            },
            {
                title: "/incident",
                url: "https://api.metromap.online/v1/incident",
                status: "U",
            },
            {
                title: "/incident/:line",
                url: "https://api.metromap.online/v1/incident/A",
                status: "U",
            },
            {
                title: "/incident/:line/:station",
                url: "https://api.metromap.online/v1/incident/A/san_antonio",
                status: "U",
            },
        ],
    },
    {
        title: "Mapa",
        data: [
            {
                title: "Embed",
                url: "https://embed.metromap.online/v1/map",
                status: "U",
            },
        ],
    },
];

export default function Status() {
    const keyId = useId();

    return (
        <div className={styles.status_table}>
            {SERVICE_LIST.map(({ title, data }) => (
                <div className={styles.status_component} key={keyId}>
                    <div className={styles.status_row}>
                        <h3>{title}</h3>
                    </div>
                    {data.map(({ title, url, status, info = null }) => (
                        <Component
                            key={keyId}
                            title={title}
                            url={url}
                            status={status}
                            info={info}
                        />
                    ))}
                </div>
            ))}
        </div>
    );
}