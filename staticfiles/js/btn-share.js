const btn_share = document.querySelectorAll('.share-all')
const news_redes = document.getElementById('redes')

const redes = [
  ['https://www.facebook.com/sharer/sharer.php?u=https://www.myruby.com.ar/','fab fa-facebook-f'],
  ['https://api.whatsapp.com/send?text=${msg} https://www.myruby.com.ar/','fab fa-whatsapp-square'],
]
function btnRedes (redes) {
  let formatRedes = `
                    <div class="col-lg-12 col-md-6 col-sm-4 text-center overlay-redes">
                      <button type="button" class="btn shadow m-2 btn-primary">
                        <a class="link-special-redes" href="${redes[0]}">
                          <i class="${redes[1]}"></i>
                          <span class="font-dark">Comparte con tus amigos!!</span>
                        </a>
                      </button>
                    </div>`
  return formatRedes
}
btn_share.forEach(item => {
  item.addEventListener('click',()=>{
    news_redes.style.display = 'block'
    const delete_btn = news_redes.innerHTML = '<button type="button" id="remove-redes" class="btn-close" aria-label="Close"></button>'
    let finalStr = ''
    for (let i in redes) {
      finalStr += btnRedes(redes[i])
      news_redes.innerHTML = delete_btn + finalStr
    }
  })
})

const wrapper = document.getElementById('wrapper')
const load = document.getElementById('load')

document.addEventListener('DOMContentLoaded',()=>{
  load.style.display = 'none'
  wrapper.classList.add('activate')
})

//Controlador del navbar
const $navbar_float = document.getElementById('navbar__nav-float')
const $navbar_mobile = document.getElementById('navbar-mobile')

window.onscroll = function(){
  const currentScroll = document.documentElement.scrollTop  //200 height to scroll
  // if(currentScroll >= 0){
  //   $navbar_float.classList.add('hiden')
  // }
  if(currentScroll >= 150){
    $navbar_mobile.classList.add('navbar__mobile-activate')
    $navbar_float.classList.add('bg-activate')
    // $navbar_float.style.display = 'block'
    if(currentScroll >= 190)
    $navbar_float.style.transform = 'translateY(45px)'
  }
  else{
    $navbar_float.classList.remove('bg-activate')
    $navbar_float.style.transform = 'translateY(-45px)'
    // $navbar_float.style.display = 'none'

  }
}

// TODO Hacer un hojo que se mueva para (Estados unido en la mira) con canva (o).


const meta = document.getElementsByTagName('meta')
for (i of meta){
  console.log(i)
}
const get_absolute_url = document.getElementById('get-absolute-url').href
const get_fb_share = document.getElementById('fb-share').setAttribute('data-href',`${get_absolute_url}`)

