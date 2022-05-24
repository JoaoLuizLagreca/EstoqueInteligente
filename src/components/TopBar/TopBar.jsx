import './TopBar.css'


export default function TopBar() {
  return (
    <div className='TopBar'>
      <div className='TopBarContainer'>
        <div className='TopBarIcon'>
           <img src='logo192.png' alt='Logo' className='logo' href='/'/>
        </div>
        <div className='MenuBar'>
          <a href='/'> Home </a>
          <a href='/CurrentState'> Estado Atual </a>
          <a href='/AddNewProducts'> Cadastro de Produtos </a>
        </div>
      </div>
    </div>
  )
}
