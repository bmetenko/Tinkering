class Introduction
    def initialize(name = "Astrid")
        @name = name
    end

    def say_hello
        if @name.nil?
            puts "Hello Noone?"
        elsif @name.respond_to?("each")
            @name.each do |iname|
                puts "Hello #{iname}!"
            end
        else
            puts "Hello #{@name}."
        end
    end

    def say_goodbye
        if @name.nil?
            puts "..."
        elsif @name.respond_to?("join")
            puts "Bye #{@name.join(", ")}."
        else
            puts "Bye #{@name}."
        end
    end

end


introducer = Introduction.new("Astro")
introducer.say_hello
introducer.say_goodbye

class Introduction
    attr_accessor :name
end

# Class extension code above
# works on initialized classes
introducer.name

# __main__ equivalent
if __FILE__ == $0
    mg = Introduction.new
    mg.say_hello
    mg.say_goodbye

    mg.name = "Observer"
    mg.say_hello
    mg.say_goodbye

    mg.name = ["Olivia", "Walter", "Peter",
    "Broyles", "Etta"]
    mg.say_hello
    mg.say_goodbye

    # Change to nil
    mg.name = nil
    mg.say_hello
    mg.say_goodbye

    a = ""
    5.times {
        a = a + "."
        print "Finished running#{a}\n"
    }

    print a + "\n"
end

exit

puts "Unreachable"
# Continue:
# https://poignant.guide/book/chapter-3.html