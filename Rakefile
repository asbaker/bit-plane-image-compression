task :test do
  system 'nosetests --nocapture'
end


task :run_combo do
  system 'python get_all_bit_planes.py images/combo.png images/combo_out'
end

task :run_text do
  system 'python get_all_bit_planes.py images/text.png images/text_out'
end

task :run_frank do
  system 'python get_all_bit_planes.py images/frank_the_tank_gray_scale.png images/frank_out'
end



task :compress_text do
  system 'python compress_gray_scale.py images/text.png images/text_out_compress.png'
end

task :compress_combo do
  system 'python compress_gray_scale.py images/combo.png images/combo_out_compress.png'
end

task :compress_frank do
  system 'python compress_gray_scale.py images/frank_the_tank_gray_scale.png images/frank_out_compress.png'
end



task :open_images do
  system 'open ./images'
end

task :clean do
  system 'rm ./images/*_out*'
  system "find . -name '*.pyc' -delete"
end
