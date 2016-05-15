<?php
const APPID = '0qUR5ShBoIBIOOBPJOZ47tk2arVFhaBQZktIUAHDAZE';
$text = $argv[1];
$to = 'ja';

$ch = curl_init('https://api.datamarket.azure.com/Bing/MicrosoftTranslator/v1/Translate?Text=%27'.urlencode($text).'%27&To=%27'.$to.'%27');
curl_setopt($ch, CURLOPT_USERPWD, APPID.':'.APPID);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($ch);
$result = explode('<d:Text m:type="Edm.String">', $result);
$result = explode('</d:Text>', $result[1]);
$result = $result[0];
echo $result;
?>
