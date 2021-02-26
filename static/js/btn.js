// Obtenemos el slug de nuestro contenido de noticias
// Cambiamos la direccion actual con el slug de noticias
document.addEventListener('DOMContentLoaded',()=>{
  const get_date_for_share_tt = document.getElementById('tt-share')
  if (get_date_for_share_tt){
    const get_absolute_url = document.getElementById('get-absolute-url').href
    // const get_fb_share = document.getElementById('fb-share')
    // get_fb_share.setAttribute('data-href',get_absolute_url)
    encode_data_for_url(get_date_for_share_tt)
  }
})

function encode_data_for_url(date){
  let data_text_a_tt = date.dataset.text
  let data_href_a_tt = date.dataset.href
  let data_via_a_tt = date.dataset.via
  let format_data_text = encodeURIComponent(data_text_a_tt)  // Search the whitespacin => '%20' equivale a ' '
  let format_data_href = encodeURIComponent(data_href_a_tt)
  return date.href = `https://twitter.com/intent/tweet?text=${format_data_text}&url=${format_data_href}&via=${data_via_a_tt}`
}