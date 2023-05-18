import React from 'react';

const Footer: React.FC = () => {
  return (
    <div className="container">
      <div className="left">
        <span>
        Copyright © {new Date().getFullYear()}{" "}
                <a href="https://metromap.online" target="_blank">
                    MetroMap Project
                </a>
                .
        </span>
      </div>
      <div className="right">
        <ul>
          <li>
            <a href="https://github.com/danielcgiraldo">Daniel Castillo Giraldo</a>
          </li>
          <li>
            <a href="https://github.com/JPortoL">Jesús Miguel Porto López</a>
          </li>
          <li>
            <a href="https://github.com/SRCrimson">Autor 3</a>
          </li>
        </ul>
      </div>

      <style jsx>{`
        .container {
          display: flex;
          justify-content: space-between;
        }
  
        .left {
          text-align: left;
          width: 50%;
        }
  
        .right {
          text-align: right;
          width: 50%;
        }
      `}</style>
    </div>
  );
};

export default Footer;