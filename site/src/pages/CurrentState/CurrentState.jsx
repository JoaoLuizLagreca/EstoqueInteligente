import "./CurrentState.css"
import MonitorWeightIcon from '@mui/icons-material/MonitorWeight';
export default function CurrentState() {
  return (
    <div className="CurrentState">
        <div className="CurrentStateContainer">
          <div className="currentStateData">
            <span className="slot">Slot 1</span>
            <MonitorWeightIcon className="WeightIcon" style={{fontSize: 500}}/>
            <span className="title">Peso Atual: </span>
            <span className="updatedDate">Ultima atualização em: </span>
            </div>
        </div>
    </div>
  )
}
