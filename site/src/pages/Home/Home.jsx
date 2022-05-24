import './Home.css';
import FeaturedInfo from '../../components/FeaturedInfo/FeaturedInfo';
import InventoryPerDate from '../../components/InventoryPerDate/InventoryPerDate';
import {InventoryData} from '../../data_test'

export default function Home() {
  return (
    <div className='Home'>
        <FeaturedInfo />
        <InventoryPerDate data={InventoryData} title='Histórico de Inventario' dataKeyX="Mes" dataKeyY="Quantidade"/>
    </div>
  )
}
