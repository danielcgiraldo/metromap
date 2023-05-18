import React, { useEffect, useState } from 'react';

const Contributors = () => {
  const [contributors, setContributors] = useState([]);

  useEffect(() => {
    const fetchContributors = async () => {
      try {
        const response = await fetch('https://api.github.com/repos/danielcgiraldo/ppi_06/contributors');
        const data = await response.json();
        setContributors(data);
      } catch (error) {
        console.error('Error al obtener los contribuidores:', error);
      }
    };

    fetchContributors();
  }, []);

  return (
    <div>
      <h2 style={{ color: '#333', textAlign: 'center', margin: '50px 0 30px 0' }}>Colaboradores</h2>
      <ul style={{ marginTop: '10px', listStyle: 'none', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: "0" }}>
        {contributors.map((contributor) => (
          <li key={contributor.id} style={{ margin: '0 15px', textAlign: 'center' }}>
            <a href={contributor.html_url} target="_blank" rel="noopener noreferrer" style={{display: "flex", alignItems: "center", flexDirection: "column", width: "100px"}}>
              <img src={contributor.avatar_url} alt={contributor.login} style={{ width: '90%', borderRadius: '50%' }} />
              <p style={{ marginTop: '10px', color: '#123' }}>{contributor.name || contributor.login}</p>
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Contributors;

