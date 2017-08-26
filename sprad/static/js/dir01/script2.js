
function allooh(athis) {
  var loginv =athis[0].children[0].value;
  var passwv =athis[0].children[1].value;

    if(validLP (loginv, passwv) == null)
      return;

   $.ajax({
      url: "/authoriz/",
      type: 'GET',
      data: {
        'userdj': loginv,
        'passworddj': passwv,
      },
      success: function (ges) {
        if (ges!='None') {
           var container = document.getElementById('container03');
                container.innerHTML ='';
           document.getElementById('brandinguser').innerHTML = ges;
        }
      else
        alert("Invalid login or password");
        }
    });
}

function regist() {
    $.ajax({
      url: "/authoriz/",
      type: 'GET',
      data: {
          'authnew': 'y',
      },
      success: function (ges) {
        if (ges!='None') {
           var container = document.getElementById('container03');
                container.innerHTML =ges;
        }
      else
        alert("error");
        }
    });
}

function registsave(athis) {
  var loginv =athis[0].children[0].value;
  var passwv =athis[0].children[1].value;

  if(validLP (loginv, passwv) == null)
      return;

  if(passwv != athis[0].children[2].value){
      alert('Пароли не совпадают');
      return;
  }

  var emailfld = athis[0].children[3].value;
if(emailfld != ''){
    var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
    if (!testEmail.test(emailfld)) {
        alert('Не корректный e-mail');
        return;
    }
}

    $.ajax({
      url: "/authoriz/",
      type: 'GET',
      data: {
          'authnews': 'y',
          'userdj': loginv,
          'passworddj': passwv,
          'email': emailfld,
      },
      success: function (ges) {
          if (ges =='y') {
              alert("Such a user exists");
              return;
          }
          if (ges =='None'){
              alert("ошибка сервера");
          }
        if (ges!='None') {
              alert("Пользователь "+loginv+" сохранён.");
            document.getElementById('brandinguser').innerHTML = loginv;
            document.getElementById('container03').innerHTML='' +
                'Welcome on our site';
        }

        }
    });

}

function validLP (loginv, passwv){
  if(!loginv || loginv.length<4){
     alert('Логин должен быть более 4х символов');
     return null;
  }
  if(!passwv || passwv.length<4){
      alert('Пароль должен быть более 4х символов');
      return null;
  }
  return 0;
}