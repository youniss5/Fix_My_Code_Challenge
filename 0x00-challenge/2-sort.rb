###
#  print and sort integers [ascending]
###

result = []
ARGV.each do |arg|
    next if arg !~ /^-?[0-9]+$/

    i_arg = arg.to_i

    is_insert = false
    i = 0
    l = result.size
    while !is_insert && i < l do
        if result[i] < i_arg
            i += 1
        else
            result.insert(i, i_arg)
            is_insert = true
            break
        end
    end
    result << i_arg if !is_insert
end

puts result

