const wrapper = document.getElementById('wrapper')
const load = document.getElementById('load')

document.addEventListener('DOMContentLoaded',()=>{
  load.style.display = 'none'
  wrapper.classList.add('activate')
  // BARS CATEGORY
  const category_radius = document.querySelector('.category-radius')
  const category_data = category_radius.dataset.toggle
  const bars = document.getElementById('bars')
  // SEEKER
  const search_radius = document.querySelector('.search-radius')
  const search_data = search_radius.dataset.toggle
  const search = document.getElementById('search-R')
  // CLASS QUERYSELECTOR
  const _category = document.querySelector('.category_')
  const $search = document.querySelector('.search_')
  btnFavorite(category_radius,bars,category_data,search_radius,search,search_data,$search)
  scrollTop()
  main_ajax()
})

function main_ajax(){
  // fas fa-exclamation con esto lo haceremos mas divertido :3
  const $error = document.querySelector('#seeker-objects .btn-submit')
  const $autocomplete = document.getElementById('autocomplete')
  document.addEventListener('keyup',(e)=>{
    const $search = document.getElementById('search')
    // objects_categories_xhr($search,$autocomplete,$error)
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
/*
para no complicarnos la vida y hacer el codigo un poco o mas limpio de lo que es, vamos hacer que sea mas simple,
como logramos eso, pues no vamos a referir a cada uno de los ID como search-[1,2,3] esto con la intencion de que
lo que vamos hacer sea mas eficaz a la hora de registro y no se nos quede tan pegado, porque creo que eso tambien
es en el rendimiento del codigo, asi que no tengamos miedo y hagamos esto mas divertido :D
*/
// function objects_categories_xhr(search,autocomplete,error){
//   const xhr = new XMLHttpRequest()
//   const method = 'GET'
//   const url = '/seeker/'
//   const responseType = 'json'
//   xhr.responseType = responseType
//   xhr.open(method,url,true)
//   xhr.onload = function(){
//     if (this.readyState == 4 && this.status == 200){
//       const server_response = this.response
//       const categories_list = server_response.response
//       for (let {category,categories} of categories_list){
//         let catgory = category
//         let catgories = categories
//         let categories_to_string = to_string(categories)
//         if (search.value !== ''){
//           if(search.value[0] === categories_to_string[0]){
//             if(categories_to_string.startsWith(search.value)){
//               error.classList.remove('error')
//               error.disabled = false
//               err(false)
//               autocomplete.classList.add('autocomplete-active')
//               return autocomplete.innerHTML = link(catgory,catgories)
//             }
//           }
//           else{
//             error.classList.add('error')
//             error.disabled = true
//             err(true)
//           }
//         }else{
//           autocomplete.classList.remove('autocomplete-active')
//           error.classList.remove('error')
//           error.disabled = false
//           err(false)
//         }
//       }
//     }
//     else if(this.status === 400){
//       // peticion invalida
//       let error = 'La respuesta de código de estado del Protocolo de Transferencia de Hipertexto (HTTP) 400 "Bad Request" indica que el servidor no puede o no procesará la petición debido a algo que es percibido como un error del cliente'
//       console.log(error)
//     }
//     else if(this.status === 500){
//       // peticion al server invalida
//       let error = `Oop! Vaya que mal, creemos que cuando la nave iba al servidor tuvo un mal percance y no pudo llegar. Dado caso a eso tenemos en este momento un ${this.status} (INTERNAL SERVER ERROR)`
//       console.error(error)
//     }
//     xhr.onerror = function(){console.error('La peticion solicitada parace no ver respondido. Por favor intentolo de nuevo status:',this.status)}
//   }
//   xhr.send()
// }
function err(error){
  const fas = document.getElementById('fas')
  if (error){
    return fas.setAttribute('class','fas fa-exclamation')
  }else{return fas.setAttribute('class','fas fa-search')}
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

function btnFavorite(category,bar,check_category,btn_search,search,check_search,addCategory){
  // BARS CATEGORY
  bar.addEventListener('click',()=>{
    if (check_category){
      check_category = false
      check_search = true
      removeClassList(btn_search,addCategory)
      return addClassList(category,addCategory)
    }else{
      check_category = true
      return removeClassList(category,addCategory)
    }
  })
  // SEEKER
  search.addEventListener('click',()=>{
    if (check_search){
      check_search = false
      check_category = true
      removeClassList(category,addCategory)
      return addClassList(btn_search,addCategory)
    }else{
      check_search = true
      return removeClassList(btn_search)
    }
  })
}
//! hacer que cuando se pulse el boton se vea la animacion hacia el OK :3
function addClassList(value,category){
  value.classList.add('active')
  // category.classList.add('active')
  value.classList.remove('deactive')
}
function removeClassList(value,category){
  value.classList.remove('active')
  // category.classList.remove('active')
  value.classList.add('deactive')
}
// CURRENT SCROLL READY
function scrollTop(){
  const arrowUp = document.getElementById('arrow-up')
  arrowUp.addEventListener('click',()=>{
    window.scrollTo({top:0,behavior:'smooth'})
  })
}