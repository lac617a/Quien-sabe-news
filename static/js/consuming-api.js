const xhr = new XMLHttpRequest();
const method = 'GET';
const url = 'api/v0.1/generic-list/';
const responseType = 'json';
xhr.responseType = responseType;
xhr.open(method,url,true);
xhr.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest")
xhr.setRequestHeader("X-Requested-With","XMLHttpRequest")
xhr.onload = function () {
  // "use strict";
  // Hacer que reconozca los errores :3
  const responseServer = this.response;
  for ({header,image} of responseServer){
    console.log(header);
  };
};
xhr.send();