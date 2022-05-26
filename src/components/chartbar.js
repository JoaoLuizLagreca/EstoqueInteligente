import { Text, View } from 'react-native'
import React, { Component } from 'react'
import { VictoryAxis, VictoryBar, VictoryChart, VictoryGroup } from "victory-native"

const data = {
  inventory: [
    { x: 'Janeiro', y: 2400 },
    { x: 'Fevereiro', y: 2210 },
    { x: 'Março', y: 2290 },
    { x: 'Abril', y: 2000 },
    { x: 'Maio', y: 2181 },
  ]
}

let XArray = []

for (let month of data.inventory){
    XArray.push(month.x)

}


export default class chartbar extends Component {
  render() {
    return (
      <View>
        <VictoryChart width={350} 
          height={220} theme={{
            axis: {
              style: {
                tickLabels: {
                  fill: '#D8DEE9',
                },
              },
            },
          }}>
          <VictoryGroup offset={15} colorScale={'qualitative'}>
          <VictoryBar
              data={data.inventory}
              animate={{
                duration: 2000,
                onLoad: { duration: 1000 },
              }}

              style={{
                data: {
                  fill: '#D8DEE9',
                  stroke: '#D8DEE9', 
                },
              }} />
            <VictoryAxis
              tickValues={XArray}
              style={{
                tickLabels: { fill: '#D8DEE9', },
                ticks: { stroke: '#D8DEE9', },
                
              }}
            />
            <VictoryAxis
              dependentAxis={true}
              style={{
                tickLabels: { fill: '#D8DEE9', },
                ticks: { stroke: '#D8DEE9', },
              }} />
          </VictoryGroup>
        </VictoryChart>
      </View>
    )
  }
}