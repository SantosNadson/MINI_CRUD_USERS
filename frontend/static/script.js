document.getElementById("btn_show_user").addEventListener("click", carregar_usuarios)
document.getElementById("insert_user").addEventListener("submit", inserir_usuarios)
document.getElementById("delete_user").addEventListener("submit", deletar_usuarios)
document.getElementById("update_user").addEventListener("submit", atualizar_usuarios);


async function carregar_usuarios() {

    const resposta = await fetch("http://localhost:8000/users/dados")

    const dados = await resposta.json()

    const lista = document.getElementById("show_users")

    lista.innerHTML = ""

    dados.forEach(tarefa => {

        const item = document.createElement("show_users")

        item.textContent = JSON.stringify(tarefa)

        lista.appendChild(item)

    })

}

async function inserir_usuarios(event){

  event.preventDefault(); // impede o envio do form
  console.log("OBTIDO: DADOS PARA CADASTRAR");
  const nome = document.getElementById("insert_name").value
  const idade = document.getElementById("insert_age").value

   const resposta = await fetch("http://localhost:8000/users/insert_dados", {
   method: "POST",
   body: JSON.stringify({
    nome,
    idade
   })

   })
   console.log('dados cadastrados')
}

async function deletar_usuarios(event){

  event.preventDefault(); // impede o envio do form
  console.log("OBTIDO: ID PARA DELETAR")
  const user_id = document.getElementById("delete_user_id").value

   const resposta = await fetch("http://localhost:8000/users/delete_dados", 
    {
   method: "DELETE",
   body: JSON.stringify({
    user_id
   })

   }
)
   console.log('dados removidos')
}

async function atualizar_usuarios(event){

   event.preventDefault(); // impede o envio do form
   console.log("OBTIDO: ID PARA ATUALIZAR")
   const user_id = document.getElementById("update_user_id").value
   const new_name = document.getElementById("update_new_name").value
   const new_age = document.getElementById("update_new_age").value

   const resposta =   fetch("http://localhost:8000/users/update_dados", 
   {
   method: "PUT",
   body: JSON.stringify({
   user_id,
   new_name,
   new_age

   })

   }
   )
   console.log('dados atualizados', user_id,new_name,new_age)
}