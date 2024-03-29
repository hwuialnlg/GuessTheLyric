import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';
import './index.css'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Home from './Home.tsx';
import Gameplay from './Gameplay.tsx';
import About from './About.tsx';
import Setup from './Setup.tsx';

// https://reactrouter.com/en/main/start/tutorial

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home/>,
  },

  {
    path: "/home",
    element: <Home/>,
  },

  {
    path: "/play",
    element: <Gameplay/>,
  },

  {
    path: "/about",
    element: <About/>,
  },

  {
    path: "/setup",
    element: <Setup/>,
  },

]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
