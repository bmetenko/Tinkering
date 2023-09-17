require 'shoes'

Shoes.app width: 500, height: 500 do

    background green..blue

    stack do
        para "MacOS app"
        
        button "Send an Alert!" do 
            alert "Alert completed!"
        end

        image "../py/1.png", 
            margin_top: 20, 
            margin_left: 20
    end

end
