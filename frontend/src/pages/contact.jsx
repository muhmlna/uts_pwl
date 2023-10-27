import React from "react";

export const Contact = () => {
  const developerInfo = {
    name: "Muhammad Maulana",
    email: "muhammad.120140080@student.itera.ac.id",
    github: "https://github.com/muhmlna",
    linkedin: "https://www.linkedin.com/in/muhammad-maulana-27b792212/",
  };

  return (
    <div className="contact">
      <h1>Contact Developer</h1>
      <p>
        Nama: {developerInfo.name}
      </p>
      <p>
        Email: <a href={`mailto:${developerInfo.email}`}>{developerInfo.email}</a>
      </p>
      <p>
        GitHub: <a href={developerInfo.github} target="_blank" rel="noopener noreferrer">{developerInfo.github}</a>
      </p>
      <p>
        LinkedIn: <a href={developerInfo.linkedin} target="_blank" rel="noopener noreferrer">{developerInfo.linkedin}</a>
      </p>
    </div>
  );
};

