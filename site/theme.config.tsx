import React from "react";
import { DocsThemeConfig, useConfig } from "nextra-theme-docs";
import { useRouter } from "next/router";
import { useUser } from '@auth0/nextjs-auth0/client';
import { Profile } from './profile';

const config: DocsThemeConfig = {
    useNextSeoProps() {
        const { asPath } = useRouter();
        if (asPath !== "/") {
            return {
                titleTemplate: "MetroMap Medellín: %s",
            };
        } else {
            return {
                titleTemplate:
                    "MetroMap: Estado de las líneas del Metro de Medellín",
                description:
                    "MetroMap es un mapa interactivo diseñado para ofrecer información en tiempo real sobre el estado de las líneas del metro de Medellín. Con una interfaz intuitiva, MetroMap permite conocer el estado de las estaciones y las posibles interrupciones del servicio.",
            };
        }
    },
    navbar: {
        extraContent: <Profile />,
        
    },
    head: () => {
        const { frontMatter } = useConfig();
        const description =
            frontMatter.description ||
            "MetroMap es un mapa interactivo diseñado para ofrecer información en tiempo real sobre el estado de las líneas del metro de Medellín. Con una interfaz intuitiva, MetroMap permite conocer el estado de las estaciones y las posibles interrupciones del servicio.";
        return (
            <>
                <meta
                    property="og:title"
                    content={
                        frontMatter.title ||
                        "MetroMap: Estado de las líneas del Metro de Medellín"
                    }
                />
                <meta
                    name="keywords"
                    content="metro, línea A, línea B, metro de medellín, medellín, mapa interactivo, estado de las líneas, interrupciones del servicio, estaciones, metrocable, bus, cable aereo"
                />
                <meta property="og:description" content={description} />
                <meta name="description" content={description} />
                <meta
                    property="og:image"
                    content="https://metromapmed.s3.amazonaws.com/assets/img/og.png"
                />
                <link
                    rel="icon"
                    href="https://metromapmed.s3.amazonaws.com/assets/img/favicon.ico"
                />
                <link
                    rel="apple-touch-icon"
                    href="https://metromapmed.s3.amazonaws.com/assets/img/logo192.png"
                />
                <meta name="author" content="metromap" />
                <meta name="robots" content="index, follow" />
            </>
        );
    },
    logo: (
        <>
            <img
                src="https://metromapmed.s3.amazonaws.com/assets/img/public/logo.svg"
                alt="MetroMap Medellín"
                id="metromap-logo"
            />
        </>
    ),
    logoLink: "https://metromap.online/",
    project: {
        link: "https://github.com/danielcgiraldo/ppi_06",
    },
    docsRepositoryBase: "https://github.com/danielcgiraldo/ppi_06/blob/main/site",
    footer: {
        text: (
            <span>
                Copyright © {new Date().getFullYear()}{" "}
                <a href="https://metromap.online" target="_blank">
                    MetroMap Project
                </a>
                .
            </span>
        ),
    },
    search: {
        placeholder: "Buscar documentación...",
    },
    toc: {
        title: "En Esta Página",
    },
    feedback: {
        content: "¿Dudas? Danos tu feedback →",
    },
    editLink: {
        text: "Edite esta página en GitHub →",
    },
    darkMode: false,
    nextThemes: {
        forcedTheme: "light"
    }
};

export default config;
