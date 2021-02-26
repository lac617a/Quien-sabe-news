document.addEventListener('DOMContentLoaded',(e)=>{
  main_ajax()
})
function main_ajax(){
  const $error_message = document.getElementById('error-message')
  const $autocomplete = document.getElementById('autocomplete')
  const $autocomplete_float = document.getElementById('autocomplete-float')
  const $search = document.getElementById('search')
  document.addEventListener('keyup',(e)=>{
    const $search_value = document.getElementById('search').value
    const $search_float_value = document.getElementById('search-float').value
    objects_categories_xhr($search,$search_value,$search_float_value,$autocomplete,$autocomplete_float,$error_message)
  })
}
const special_characters = /[`~!@#$%^&*()_\-+=\[\]{};:'"\\|\/,.<>?\s]/g
const Cut_the_spaces = /^\s+|\s+$/g
// remove accents.
const from = "àáäâèéëêìíïîòóöôùúüûñç·/_,:;"
const to   = "aaaaeeeeiiiioooouuuunc------"

const string_to_slug = (slug)=>{
  slug = slug.replace(special_characters,' ').toLowerCase() // Reemplaza los caracteres especiales | simbolos con un espacio
  slug = slug.replace(Cut_the_spaces,'') // Corta los espacios al inicio y al final del sluging
  for(let i=0,l=from.length;i<l;i++){slug = slug.replace(new RegExp(from.charAt(i),'g'),to.charAt(i))}
  slug = slug.replace(/[^a-z0-9 -]/g,'') // remove invalid chars
  .replace(/\s+/g,'-') // remplazar espacios blancos de -
  .replace(/-+/g,'-') // remplazar dashes
  return slug
}

function to_string(str){
  str = str.replace(special_characters,' ').toLowerCase() // Reemplaza los caracteres especiales | simbolos con un espacio
  str = str.replace(Cut_the_spaces,'') // Corta los espacios al inicio y al final del sluging
  for(let i=0,l=from.length;i<l;i++){str = str.replace(new RegExp(from.charAt(i),'g'),to.charAt(i))}
  return str
}
function objects_categories_xhr(search,search_value,search_float,autocomplete,autocomplete_float,error_message){
  const xhr = new XMLHttpRequest()
  const method = 'GET'
  const url = '/seeker/'
  const responseType = 'json'
  xhr.responseType = responseType
  xhr.open(method,url,true)
  xhr.onload = function(){
    if (this.readyState == 4 && this.status == 200){
      const server_response = this.response
      const categories_list = server_response.response
      for (let {category,categories} of categories_list){
        let catgory = category
        let catgories = categories
        let categories_to_string = to_string(categories)
        if(search_value[0] === categories_to_string[0] || search_float[0] === categories_to_string[0]){
          if(categories_to_string.startsWith(search_value) && search_value !== ''){
            error_message.classList.remove('message-active')
            search.classList.remove('item-not-found')
            autocomplete.classList.add('autocomplete-active')
            return autocomplete.innerHTML = link(catgory,catgories)
          }
          else if(categories_to_string.startsWith(search_float) && search_float !== ''){
            autocomplete_float.classList.add('autocomplete-active')
            return autocomplete_float.innerHTML = link(catgory,catgories)
          }
        }
        else if(search_value === ''){
          autocomplete.classList.remove('autocomplete-active')
          error_message.classList.remove('message-active')
          search.classList.remove('item-not-found')
        }
        else{
          error_message.classList.add('message-active')
          search.classList.add('item-not-found')
        }
      }
    }
    else if(this.status === 400){
      // peticion invalida
      let error = 'La respuesta de código de estado del Protocolo de Transferencia de Hipertexto (HTTP) 400 "Bad Request" indica que el servidor no puede o no procesará la petición debido a algo que es percibido como un error del cliente'
      console.log(error)
    }
    else if(this.status === 500){
      // peticion al server invalida
      let error = `Oop! Vaya que mal, creemos que cuando la nave iba al servidor tuvo un mal percance y no pudo llegar. Dado caso a eso tenemos en este momento un ${this.status} (INTERNAL SERVER ERROR)`
      console.error(error)
    }
    xhr.onerror = function(){console.error('La peticion solicitada parace no ver respondido. Por favor intentolo de nuevo status:',this.status)}
  }
  xhr.send()
}

function link(pattern,url) {
  return `<ul class="list-group">
            <li class="nav-item">
              <i class="fas fa-search" style="font-size:14px;opacity:.7;"></i>
              <a class="nav-link-search" href="/Category/${string_to_slug(pattern)}/${string_to_slug(url)}/">
              <span>${url}</span>
              </a>
            </li>
          </ul>`
}