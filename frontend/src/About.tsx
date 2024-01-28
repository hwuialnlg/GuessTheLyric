// import Navbar from './components/Navbar';
import './App.css'
import image from './assets/hackathon.jpg'
import { Link } from 'react-router-dom';

function About()
{
    return (
        <div className="mainLayer">
            
            <div className="topLayer">
                <Link to="/" style={{textDecoration: 1, color: 'inherit'}}>
                <h1>About Us</h1>
                </Link>
            </div>
            
            
            <div className="bottomLayer">
                <img src={image} className="usJPG"/>
                <p className="aboutUs">
                At Irvine Hacks 2024, a thrilling hackathon, three ingenious Software Engineers from the University of California, Irvine embarked on a mission: to craft a captivating game centered around guessing lyrics from beloved songs. Among them were the talented trio: Andy, Devesh, and Will. While Andy and Will delved deep into backend development, Devesh expertly sculpted the frontend landscape. Their frontend arsenal boasted the dynamic trio of React.js, Vite, and TypeScript, while the backend fortress was fortified with the robust foundations of Python and Flask. 🚀🎶
                </p>
            </div>

        </div>
    )
}

export default About;