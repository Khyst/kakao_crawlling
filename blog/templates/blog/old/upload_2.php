<?
//업로드한 파일을 저장할 디렉토리
$save_dir = "files/";

//파일이 HTTP POST 방식을 통해 정상적으로 업로드되었는지 확인한다.
if(is_uploaded_file($_FILES["myFile"]["tmp_name"]))
{
   echo "uploaded file name : ".$_FILES["myFile"]["name"] ."\n
";
   echo "uploaded file volume : ".$_FILES["myFile"]["size"] ."\n
";
   echo "uploaded file name MIME Type : ".$_FILES["myFile"]["type"] ."\n
";
   echo "saved temporary directory file name : ".$_FILES["myFile"]["tmp_name"]."
\n";

   //파일을 저장할 디렉토리 및 파일명
   $dest = $save_dir . $_FILES["myFile"]["name"];

   //파일을 지정한 디렉토리에 저장
   if(!move_uploaded_file($_FILES["myFile"]["tmp_name"], $dest))
   {
      die("파일을 지정한 디렉토리에 저장하는데 실패했습니다.");
   }
}
?>
