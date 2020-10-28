document.addEventListener("DOMContentLoaded",()=>{

    var input_img = document.querySelector('#file-input');
    input_img.addEventListener('change',preview);
    
    function preview(){

    var fileObject=this.files[0];
    var fileReader=new FileReader();
    fileReader.readAsDataURL(fileObject);

    fileReader.onload = ()=> {
        var result=fileReader.result;
        var img=document.querySelector('#preview');
        img.setAttribute('src',result);
    }
}
    

    document.getElementById("classify-button").onclick = ()=>{                
        
        var fileDecode=new FileReader();
        fileDecode.onload= ()=> {

            var data=fileDecode.result;            
            data=data.replace("data:image/jpeg;base64,",'');          
            var Data=JSON.stringify({'data':data}); 

            var request=new XMLHttpRequest();
            request.onload = ()=>{                      
            
                var result=request.responseText;
                document.getElementById('base64').innerHTML=result;
                
            }    
            
            request.open('POST','/predict');
            request.send(Data);
            delete request;
            delete Data;
        }     
         
        var img= input_img.files[0];
        fileDecode.readAsDataURL(img);

    }
});
