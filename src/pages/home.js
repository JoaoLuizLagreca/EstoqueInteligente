import React,{useState} from "react";
import {
    Text, 
    StyleSheet, 
    SafeAreaView, 
} from 'react-native';
import InventoryPerMonth from '../components/chartbar'

export function Home(){

  return(
      
    <SafeAreaView style={styles.container}>
      
      <Text style={styles.title}>
          Welcome, %Username%
      </Text>
      <SafeAreaView style={styles.bigNumbers}>
        
        <SafeAreaView style={styles.numberBox}>
            <Text style={[styles.textSkill, {margin: 20}]}>
                Estoque Atual:
            </Text>

            <Text style={styles.stockNumber}>
                10
            </Text>
        </SafeAreaView>

        {/* segunda caixa de texto */}

        <SafeAreaView style={styles.numberBox}>
            <Text style={[styles.textSkill, {margin: 20}]}>
                Estoque Final:
            </Text>

            <Text style={styles.stockNumber}>
                1000
            </Text>
        </SafeAreaView>

      </SafeAreaView>
      
      <SafeAreaView style={styles.chart} >
            <Text style={styles.sub_title}>Estoque X Mês</Text>
            <InventoryPerMonth />
      </SafeAreaView>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({

    container: {
        flex: 1, 
        backgroundColor: '#242933',
        paddingHorizontal: 20,
        paddingVertical: 70,
        paddingHorizontal:30
    },
    title: {
        color: '#D8DEE9',
        fontSize: 28,
        fontWeight:'bold'
    },
    sub_title: {
        color: '#D8DEE9',
        fontSize: 22,
        fontWeight:'bold',
        margin: 20
    },
    textSkill: {
        color:'#D8DEE9',
        fontSize: 16,
        fontWeight: 'bold',
    },
    bigNumbers: {
        marginTop: 15,
        flexDirection: 'row',
    },

    numberBox: {
        marginHorizontal: 5,
        backgroundColor: '#2E3440',
        borderRadius:7,
        width: '47%',
        alignItems: 'center'      
    },

    chart: {
        marginVertical: 20,
        backgroundColor: '#2E3440',
        borderRadius:7,
        height:'50%'
    },
    stockNumber: {
        color: '#D8DEE9',
        fontSize: 32,
        fontWeight: 'bold',
        paddingVertical: 6,
        marginBottom: 8
    }
});