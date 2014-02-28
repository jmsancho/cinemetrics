#!/usr/bin/env ruby
require "srt"
require "sanitize"

REJECT_LINES = [/Best watched using Open Subtitles MKV Player/,
  /Subtitles downloaded from www.OpenSubtitles.org/, /^Subtitles by/,
  /www.tvsubtitles.net/, /subtitling@bbc.co.uk/, /addic7ed/, /allsubs.org/,
  /www.seriessub.com/, /www.transcripts.subtitle.me.uk/, /~ Bad Wolf Team/,
  /^Transcript by/, /^Update by /, /UKsubtitles.ru/
]

fname = ARGV[0]
file = SRT::File.parse(File.new(fname))
file.lines.each do |line|
  txt = line.text.reject do |l|
    if l =~ /^OK/ # OK. et al.
      false
    elsif l =~ /[\?\.!]$/ # keeps screaming, includes some sounds
      false
    else
      #l =~ /^[^a-z]*$/ # Reject all-upcase lines to remove sound descriptions
      false
    end
  end
  txt = txt.join(" ").encode("UTF-8")
  txt.gsub!(" .", ".") # . . . ellipsis
  txt.gsub!("\u0092", "'") # RIGHT SINGLE QUOTATION MARK apostrophe
  txt = txt.strip.squeeze(" ")

  next if txt.empty?
  next if REJECT_LINES.any? { |expr| expr =~ txt }

  puts Sanitize.clean(txt)
end
puts
