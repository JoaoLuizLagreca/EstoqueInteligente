import './App.css';
import TopBar from './components/TopBar/TopBar';
import Home from './pages/Home/Home';
import CurrentState from './pages/CurrentState/CurrentState';
import AddNewProducts from './pages/AddNewProduct/AddNewProducts';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";

function App() {
  return (
    <div className='Container'>
    <TopBar />
      <Router>
        <Routes >
          <Route exact path='/' element={<Home />} />
          <Route path='/CurrentState' element={<CurrentState />} />
          <Route path='/AddNewProducts' element={<AddNewProducts />} />
          
        </Routes>

      </Router>
    </div>
  );
}

export default App;
