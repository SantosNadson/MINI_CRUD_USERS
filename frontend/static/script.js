document.getElementById("btn_show_user").addEventListener("click", load_users)
document.getElementById("insert_user").addEventListener("submit", insert_user)
document.getElementById("delete_user").addEventListener("submit", delete_user)
document.getElementById("update_user").addEventListener("submit", update_user);


async function load_users() {

    const response = await fetch("http://localhost:8000/users/dados")

    const data = await response.json()

    const list = document.getElementById("show_users")

    list.innerHTML = ""

    data.forEach(user => {
    const item = document.createElement("li")
    item.innerHTML = `
        <strong>ID:</strong> ${user.id}<br>
        <strong>Nome:</strong> ${user.nome}<br>
        <strong>Idade:</strong> ${user.idade}
    `
    list.appendChild(item)
})

}

async function insert_user(event){

  event.preventDefault();
  console.log("OBTAINED: USER DATA TO REGISTER");
  const name = document.getElementById("insert_name").value
  const age = document.getElementById("insert_age").value

   const response = await fetch("http://localhost:8000/users/insert_dados", {
   method: "POST",
   body: JSON.stringify({
    nome: name,
    idade: age
   })

   })
   console.log('User registered successfully')
}

async function delete_user(event){

  event.preventDefault();
  console.log("OBTAINED: USER ID TO DELETE")
  const user_id = document.getElementById("delete_user_id").value

   const response = await fetch("http://localhost:8000/users/delete_dados", 
    {
   method: "DELETE",
   body: JSON.stringify({
    user_id
   })

   }
)
   console.log('User deleted successfully')
}

async function update_user(event){

   event.preventDefault();
   console.log("OBTAINED: USER ID TO UPDATE")
   const user_id = document.getElementById("update_user_id").value
   const new_name = document.getElementById("update_new_name").value
   const new_age = document.getElementById("update_new_age").value

   const response = await fetch("http://localhost:8000/users/update_dados", 
   {
   method: "PUT",
   body: JSON.stringify({
   user_id,
   new_name,
   new_age

   })

   }
   )
   console.log('User updated successfully', user_id, new_name, new_age)
}