<?php

// 설정
$uploads_dir = '/uploads';
$allowed_ext = array('jpg','jpeg','png','gif', 'hwp', 'pdf');

// 오류 확인
if( !isset($_FILES['myfile']['error']) ) {
	echo json_encode( array(
		'status' => 'error',
		'message' => '파일이 첨부되지 않았습니다.'
	));
	exit;
}

$error = $_FILES['myfile']['error'];
if( $error != UPLOAD_ERR_OK ) {
	switch( $error ) {
		case UPLOAD_ERR_INI_SIZE:
		case UPLOAD_ERR_FORM_SIZE:
			$message = "파일이 너무 큽니다. ($error)";
			break;
		case UPLOAD_ERR_NO_FILE:
			$message = "파일이 첨부되지 않았습니다. ($error)";
			break;
		default:
			$message = "파일이 제대로 업로드되지 않았습니다. ($error)";
	}
	echo json_encode( array(
		'status' => 'error',
		'message' => $message
	));
	exit;
}

//! 오류없음 확인 파일전송 !

// 변수 정리
$name = $_FILES['myfile']['name'];
$ext = array_pop(explode('.', $name));

// 확장자 확인
if( !in_array($ext, $allowed_ext) ) {
	echo json_encode( array(
		'status' => 'error',
		'message' => '허용되지 않는 확장자입니다.'
	));
	exit;
}

// 파일 이동
move_uploaded_file( $_FILES['myfile']['tmp_name'], "$uploads_dir/$name");

// 파일 정보 출력
echo json_encode( array(
	'status' => 'OK',
	'name' => $name,
	'ext' => $ext,
	'type' => $_FILES['myfile']['type'],
	'size' => $_FILES['myfile']['size']
));
