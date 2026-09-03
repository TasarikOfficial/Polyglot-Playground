hue = (ARGV[0] || rand(360)).to_i % 360
puts "Palette for hue #{hue}"
[15, 35, 55, 72, 88].each_with_index do |light, i|
  puts "shade-#{(i+1)*100}: hsl(#{hue} 80% #{light}%)"
end
