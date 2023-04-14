import styles from "./map.module.css";

export default function Map() {

    return (
        <iframe className={styles.map} style={{aspectRatio: "3/4"}} src="https://embed.metromap.online/v1/map?public-key=test" />
    )
}
