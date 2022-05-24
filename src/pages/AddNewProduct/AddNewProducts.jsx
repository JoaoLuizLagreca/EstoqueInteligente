import './AddNewProducts.css'

export default function AddNewProducts() {
  return (
    <div className="AddNewProducts">
      <div className="AddNewProductContainer">
        <div className="FormContainer">
        <div className="textContent">
          <span className="titleOfReg">Cadastro de Novos Produtos</span>
          <span className="subtitle">Insira ao lado as informações de novos produtos</span>
        </div>
          <form action="" method="post" className='FormAddNewProduct'>
            <fieldset>
              <legend>Nome Do Produto</legend>
              <input type="text" name='NomeDoProduto' autoFocus placeholder='Digite o Nome do produto' required/>
            </fieldset>
            
            <fieldset>
              <legend>Peso Médio</legend>
              <input type="number" name="pesoMedio" id="pesoMedio" step="0.01" inputMode='numeric'required/>
            </fieldset>

            <fieldset>
              <legend>Preço</legend>
              <input type="number" name="price" id="price" step="0.01" inputMode='numeric' required/>
            </fieldset>

            <fieldset>
              <legend>Quantidade em Estoque</legend>
              <input type="number" name="amount" id="amount" inputMode='numeric' required/>
            </fieldset>
            
            <button type="submit">Cadastrar um Produto</button>  
          
          </form>
        </div>
      </div>
    </div>
  )
}
