import { useState, useEffect } from 'react';
import { Briefcase, GraduationCap, Gamepad2, MapPin, User, Camera } from 'lucide-react';
import img1 from './assets/IMG_2402.jpg';
import img2 from './assets/IMG_2488.jpg';
import img3 from './assets/IMG_2493.jpg';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import './styles/App.css';

// Fix for default marker icons in React Leaflet
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

function App() {
  const [activeTab, setActiveTab] = useState('about');
  const [data, setData] = useState({
    experiences: [],
    education: [],
    hobbies: [],
    locations: []
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // In development mode, proxying isn't set up yet so we just mock data or assume production
    // Since Flask and React are running on different ports during dev, we'd need CORS.
    // For simplicity, we fetch relative path which works after build.
    fetch('/api/portfolio')
      .then(res => res.json())
      .then(fetchedData => {
        setData(fetchedData);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching data:', err);
        // Fallback data for local dev without Flask running on same port
        setData({
          experiences: [
            { title: "Software Engineering Intern", company: "TD", duration: "May 2026 - Aug 2026", description: "QE Dev Tooling" },
            { title: "Software Engineering Intern", company: "BMO", duration: "Sep 2025 - April 2026", description: "Cloud Development" },
            { title: "Software Engineering Intern", company: "Roche", duration: "Jan 2025 - Aug 2025", description: "First intern hire in PDIE!" }
          ],
          education: [
            { school: "University of Western Ontario", degree: "B.S. Computer Science", duration: "2022 - 2027" }
          ],
          hobbies: [
            { name: "Skateboarding", description: "Cruising the streets and trying new tricks at the local park." },
            { name: "Volleyball", description: "Playing setter for my intramural team. Always down for a beach game." },
            { name: "Gaming", description: "Currently grinding ranked in Valorant. I mostly play FPS games." }
          ],
          locations: [
            { lat: 39.3999, lng: -8.2245, name: "Portugal" },
            { lat: 49.2827, lng: -123.1207, name: "Vancouver" },
            { lat: 53.9333, lng: -116.5765, name: "Alberta" },
            { lat: 49.8951, lng: -97.1384, name: "Winnipeg" },
            { lat: 27.9944, lng: -81.7603, name: "Florida" },
            { lat: 35.8617, lng: 104.1954, name: "China" },
            { lat: 22.3193, lng: 114.1694, name: "Hong Kong" },
            { lat: 23.1291, lng: 113.2644, name: "Guangzhou" },
            { lat: 22.1987, lng: 113.5439, name: "Macau" },
            { lat: 18.7357, lng: -70.1627, name: "Dominican Republic" },
            { lat: 25.0343, lng: -77.3963, name: "Bahamas" }
          ]
        });
        setLoading(false);
      });
  }, []);

  const tabs = [
    { id: 'about', label: 'About', icon: <User size={20} /> },
    { id: 'experience', label: 'Experience', icon: <Briefcase size={20} /> },
    { id: 'hobbies', label: 'Hobbies', icon: <Gamepad2 size={20} /> },
    { id: 'map', label: 'Travel Map', icon: <MapPin size={20} /> }
  ];

  return (
    <div className="app-container">
      <header className="header">
        <div className="header-content">
          <div className="logo-section">
            <div className="logo-placeholder">CX</div>
            <h1>Chandler Xie</h1>
          </div>
          <p className="tagline">Software Engineer & MLH Fellow</p>
        </div>
      </header>

      <main className="main-content">
        <div className="tabs-container">
          <nav className="tab-nav">
            {tabs.map(tab => (
              <button
                key={tab.id}
                className={`tab-btn ${activeTab === tab.id ? 'active' : ''}`}
                onClick={() => setActiveTab(tab.id)}
              >
                {tab.icon}
                <span>{tab.label}</span>
              </button>
            ))}
          </nav>

          <div className="tab-content-area">
            {loading ? (
              <div className="loader-container">
                <div className="spinner"></div>
              </div>
            ) : (
              <>
                {activeTab === 'about' && (
                  <section className="animate-fade-in content-section">
                    <h2>Hello, I'm Chandler!</h2>
                    <p className="bio-text">
                      I'm a passionate Software Engineer currently studying Computer Science at the University of Western Ontario. 
                      I enjoy building scalable backend systems, exploring cloud development, and creating seamless user experiences. 
                      Outside of coding, you'll probably find me skateboarding, hitting the volleyball courts, or grinding Valorant.
                    </p>
                    
                    <div className="education-container mt-6">
                      <h3 className="section-subtitle"><GraduationCap className="inline-icon" /> Education</h3>
                      {data.education.map((edu, idx) => (
                        <div key={idx} className="card edu-card">
                          <h4>{edu.school}</h4>
                          <p className="card-meta">{edu.degree} &middot; {edu.duration}</p>
                        </div>
                      ))}
                    </div>

                    <div className="about-photos mt-6">
                      <h3 className="section-subtitle"><Camera className="inline-icon" /> Snapshots</h3>
                      <div className="photo-grid">
                        <img src={img1} alt="About me 1" className="about-photo" />
                        <img src={img2} alt="About me 2" className="about-photo" />
                        <img src={img3} alt="About me 3" className="about-photo" />
                      </div>
                    </div>
                  </section>
                )}

                {activeTab === 'experience' && (
                  <section className="animate-fade-in content-section">
                    <h2>Work Experience</h2>
                    <div className="cards-list">
                      {data.experiences.map((exp, idx) => (
                        <div key={idx} className="card exp-card">
                          <div className="card-header">
                            <h4>{exp.title}</h4>
                            <span className="duration-badge">{exp.duration}</span>
                          </div>
                          <p className="company">{exp.company}</p>
                          <p className="description">{exp.description}</p>
                        </div>
                      ))}
                    </div>
                  </section>
                )}

                {activeTab === 'hobbies' && (
                  <section className="animate-fade-in content-section">
                    <h2>My Hobbies</h2>
                    <div className="hobbies-grid">
                      {data.hobbies.map((hobby, idx) => (
                        <div key={idx} className="hobby-card">
                          <div className="hobby-info">
                            <h4>{hobby.name}</h4>
                            <p>{hobby.description}</p>
                          </div>
                        </div>
                      ))}
                    </div>
                  </section>
                )}

                {activeTab === 'map' && (
                  <section className="animate-fade-in content-section map-wrapper">
                    <h2>Places I've Explored</h2>
                    <div className="map-container">
                      <MapContainer center={[35, 0]} zoom={2} style={{ height: '450px', width: '100%' }}>
                        <TileLayer
                          url="https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png"
                          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
                        />
                        {data.locations.map((loc, idx) => (
                          <Marker key={idx} position={[loc.lat, loc.lng]}>
                            <Popup>{loc.name}</Popup>
                          </Marker>
                        ))}
                      </MapContainer>
                    </div>
                  </section>
                )}
              </>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
