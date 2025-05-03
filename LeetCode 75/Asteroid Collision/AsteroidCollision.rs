impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut survivors=Vec::new();
        for rock in asteroids{
            let mut boom=false;
            while !survivors.is_empty()&&survivors.last().unwrap()>&0&& rock<0{
                let last_rock:i32=*survivors.last().unwrap();
                if last_rock.abs()>rock.abs(){
                    boom=true;
                    break;
                }
                else if last_rock.abs()<rock.abs(){
                    survivors.pop();
                }
                else{
                    survivors.pop();
                    boom=true;
                    break;
                }
            }
            if !boom{
                survivors.push(rock);
            }
        }
        survivors
    }
}

//QED
//Problem 735 (Medium of Asteroid Collision) - Jason Balayev (rust)