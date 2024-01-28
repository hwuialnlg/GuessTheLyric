import Navbar from "./components/Navbar";
import { Link } from 'react-router-dom';

function Home(){
    // const options = ["Play, Leaderboards, About"];
    return (
        <div className="home-wrapper">
            <Navbar/>

            <div className="menu-items">
                <div className="menu-option">
                    <Link to="/setup" style={{ color: 'inherit', textDecoration: 'inherit'}}><p>Play</p></Link>                
                </div>

                <div className="menu-option">
                <Link to="/about" style={{ color: 'inherit', textDecoration: 'inherit'}}><p>Leaderboard</p></Link>                
                </div>
                
                <div className="menu-option">
                    <Link to="/about" style={{ color: 'inherit', textDecoration: 'inherit'}}><p>About</p></Link>                
                </div>
            </div>
        </div>

    )
}

export default Home;