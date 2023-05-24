import styles from "./map.module.css";

export default function Map() {
    // Configure how the map is showed
    return (
        <iframe className={styles.map} style={{aspectRatio: "3/4"}} src="https://embed.metromap.online/v1/map?public-key=4ff4747e398be349379c" />
    )
}
