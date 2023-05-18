import styles from "./map.module.css";

export default function Map() {

    return (
        <iframe className={styles.map} style={{aspectRatio: "3/4"}} src="http://embed.metromap.local:8000/v1/map?public-key=0f0e691a275bd4140752" />
    )
}
