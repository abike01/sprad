/**
 * Created by ab01 on 7/8/2017.
 */

$(document).ready(function(){
    afterload();

    $(document).on("click", "#eventsTable2 tr", function(e) {
        var thChNodes = this.childNodes[0];
        if($(this).parent().parent().attr('id')=== 'eventsTable2') {

            var theThis = thChNodes.parentNode;
            var nextThis =$(theThis).closest('tr');

            if (nextThis.next('tr')[0] != undefined && nextThis.next('tr')[0].childNodes[0].innerHTML === '') {
                nextThis.next('tr').remove();
                return;
            }
            if (thChNodes.innerText != '') {
                $.ajax({
                    url: "/get_scipt/",
                    type: 'GET',
                    data: {
                        'tid': thChNodes.innerText,
                        'csrftoken': document.getElementsByName("csrfmiddlewaretoken")[0].value,
                    },
                    success: function (json) {
                        if (json != 'None') {
                            json = JSON.parse(json);
                            tRow='';
            for (var key in json) {
                let getl = json[key];
                let women ='';

                if(getl['f3'].toLowerCase() =='women')
                   women ='bgcolor="#FBACAC"';
                   tRow += '<tr '+women+'><td style="display:none;">'+getl['f1']+'</td>' +
                       '<td style="display:none;"></td><td>' + getl['f2'] + '; ' + getl['f3'] + '</td></tr>';
            }
            tRow = '<table id=\'eventsTable3\'>' + tRow + '</table>';

            var tRow = '<tr><td></td><td>' + tRow + '</td></tr>';
            nextThis.after(tRow);
                        }
                        else
                            alert("No data");
                    }
                });
            }
        }
if($(this).parent().parent().attr('id')=== 'eventsTable3') {
   $.ajax({
      url: "/get_scipt/",
      type: 'GET',
      data: {
        'mid': thChNodes.innerText,
        'csrftoken': document.getElementsByName("csrfmiddlewaretoken")[0].value,
      },
      success: function (ges) {
        if (ges!='None') {
           var container = document.getElementById('container03');
           if(ges.indexOf('<div')!=-1){
                container.innerHTML =ges;
           }
        else{
   var partxt ='<b>'+thChNodes.parentNode.children[2].innerHTML+'</b>';
   createDetailsRep(container,ges,thChNodes.innerText,partxt);
           }
      }
      else
        alert("No data");
        }
    });
}
    });

   $("#button01").click(function(){
     afterload()
   });

function afterload() {
//    $( "#container02" ).text( "The DOM is now loaded and can be manipulated." );
   $.ajax({
     url: "/get_scipt/",
     type: 'GET',
     data: {
       'par1': 'obana',
       'csrftoken': document.getElementsByName("csrfmiddlewaretoken")[0].value,
     },
     success: function (json) {
       if (json!='None') {
        json=JSON.parse(json);
        var container = document.getElementById('container02');
        createTree(container, json, 'eventsTable2' );
        }
        else
           alert("No data");
     }
    });
}

function createTree(container, obj, nameTab) {
    container.innerHTML = createTreeText(obj, nameTab);
}

function createTreeText(obj, nameTab) {

   let tbL =createTr(obj);

   if (tbL) {//style="cursor:pointer"
       var ul = '<table id="'+nameTab+'" style="cursor:pointer"' +//
           ' class="table table-hover" class="table-condensed table-striped" >'+
     tbL + '</table>';
   }

     return ul || '';
 }

 function createTr(obj) {
    let tRow ='';
    for (var key in obj) {
      let getl =obj[key];
      tRow += '<tr><td style="display:none;">'+getl['f1']+'</td>' + // style=".selected{ background: silver;}
          '<td>' + (key*1+1) +'</td><td>'+ getl['f3'] + '</td></tr>';
    }
    return tRow;
 }

});

function createDetailsRep(container, obj, ids,partxt) {
   obj=JSON.parse(obj);
  let titulDiv ='<button type="button" class="btn-small btn-info" onclick="delDetailsAcordion(\''+ids+'\');">x</button>&nbsp';
    titulDiv+='<a data-toggle="collapse" data-target="#'+ids+'" href="" >'+partxt+'; '+obj[0][0]+'</a>';
  let getDiv=obj[0][1].substring(0,10)+' '+obj[0][2]+'<br> '+obj[0][10]+' - '+obj[0][11]+' <br> '+obj[0][9];
  let inHtmls='<div style="border:1px solid #0ecff2;" id="'+ids+'" class="expand">';
   inHtmls+=getDiv+'</div>';

  var child_th=container.getElementsByTagName('*');
  for(var i=0; i<child_th.length; i++)
      if(child_th[i].id==ids){
         child_th[i].innerHTML=getDiv; //inHtmls;
         return;
      }
     container.innerHTML =
         container.innerHTML+ '<div id="'+ids+'_div" style="background-color: #fff1e8;">'+titulDiv+ inHtmls+'</div>';
      //border:1px solid #0ecff2;
}

function delDetailsAcordion(ids) {
  idElem = document.getElementById(ids+'_div');
  idElem.parentNode.removeChild(idElem);
}
//============================================================
/*
//    $(function () {
 //   var $result = $('#eventsResult');

    $('#eventsTable').on('all.bs.table', function (e, name, args) {
        console.log('Event:', name, ', data:', args);
    })
    .on('click-row.bs.table', function (e, row, $element) {
        console.log('Event: click-row.bs.table');
    })
    .on('dbl-click-row.bs.table', function (e, row, $element) {
        console.log('Event: dbl-click-row.bs.table');
    })
    .on('sort.bs.table', function (e, name, order) {
        console.log('Event: sort.bs.table');
    })
    .on('check.bs.table', function (e, row) {
        console.log('Event: check.bs.table');
    })
    .on('uncheck.bs.table', function (e, row) {
        console.log('Event: uncheck.bs.table');
    })
    .on('check-all.bs.table', function (e) {
        console.log('Event: check-all.bs.table');
    })
    .on('uncheck-all.bs.table', function (e) {
        $result.text('Event: uncheck-all.bs.table');
    })
    .on('load-success.bs.table', function (e, data) {
        console.log('Event: load-success.bs.table');
    })
    .on('load-error.bs.table', function (e, status) {
        console.log('Event: load-error.bs.table');
    })
    .on('column-switch.bs.table', function (e, field, checked) {
        console.log('Event: column-switch.bs.table');
    })
    .on('page-change.bs.table', function (e, number, size) {
        console.log('Event: page-change.bs.table');
    })
    .on('search.bs.table', function (e, text) {
        console.log('Event: search.bs.table');
    });
//});
*/
