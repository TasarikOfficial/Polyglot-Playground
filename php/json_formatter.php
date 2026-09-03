<?php
if ($argc < 2) { exit("Usage: php json_formatter.php <file>\n"); }
$data = json_decode(file_get_contents($argv[1]), true);
if (json_last_error() !== JSON_ERROR_NONE) { exit("Invalid JSON: ".json_last_error_msg()."\n"); }
echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES).PHP_EOL;
