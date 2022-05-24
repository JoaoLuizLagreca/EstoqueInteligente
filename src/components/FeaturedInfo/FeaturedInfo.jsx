import './FeaturedInfo.css'
import {ArrowDownward, ArrowUpward} from '@material-ui/icons'

export default function FeaturedInfo() {
  return (
    <div className='featured'>
        <div className="featuredItem">
            <span className='featureTitle'>Balanço de Inventario</span>
            <div className='featureDataContainer'>
                <span className='featureData'> 15 unidades</span>
                <span className='featureDataRate'> -2 <ArrowDownward className='featuredIconNegative'/> </span>
            </div>
            <span className='featuredSub'>Comparativo do dia</span>
        </div>

        <div className="featuredItem">
          <span className='featureTitle'>Balanço Financeiro</span>
          <div className='featureDataContainer'>
              <span className='featureData'> R$ 16,00</span>
              <span className='featureDataRate'> + R$2,00 <ArrowUpward className='featuredIconPositive'/> </span>
          </div>
          <span className='featuredSub'>Comparativo do dia</span>
        </div>
        
        <div className="featuredItem">
          <span className='featureTitle'>Balanço Financeiro</span>
          <div className='featureDataContainer'>
              <span className='featureData'> R$ 16,00</span>
              <span className='featureDataRate'> + R$2,00 <ArrowUpward className='featuredIconPositive'/> </span>
          </div>
          <span className='featuredSub'>Comparativo do dia</span>
        </div>
      </div>

    
  )
}
