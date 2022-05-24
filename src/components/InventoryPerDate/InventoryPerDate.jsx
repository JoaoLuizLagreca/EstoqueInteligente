import '../InventoryPerDate/InventoryPerDate.css'
import { BarChart, Bar,  XAxis, ResponsiveContainer, YAxis, Tooltip, CartesianGrid } from 'recharts';


export default function InventoryPerDate({title, data, dataKeyX,dataKeyY, grid}) {
  return (
      <div className="InventoryPerDate">
        <div className="ChartContainer">
            <div className='ChartTitle'>
                <span className='title'>{title}</span>
            </div>
            <ResponsiveContainer width="100%" aspect={4/1}>
                <BarChart data={data}>
                    <Tooltip cursor={false}/>
                    <XAxis dataKey={dataKeyX} stroke="#ECEFF4" />
                    <YAxis dataKey={dataKeyY} stroke="#ECEFF4" />
                    <Bar type="monotone" dataKey={dataKeyY} fill="#5E6A82" />
                    {grid&&<CartesianGrid stroke='#D8DEE9' strokeDashoffset="5 5" />}
                </BarChart>
            </ResponsiveContainer>
        </div>
    </div>
  )
}

