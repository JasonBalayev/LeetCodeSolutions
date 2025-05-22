impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let r=matrix.len();
        let c=matrix[0].len();
        let mut first_r=false;
        let mut first_c=false;
        for j in 0..c{
            if matrix[0][j]==0{
                first_r=true;
                break;
            }
        }
        for i in 0..r{
            if matrix[i][0]==0{
                first_c=true;
                break;
            }
        }
        for i in 1..r{
            for j in 1..c{
                if matrix[i][j]==0{
                    matrix[i][0]=0;
                    matrix[0][j]=0;
                }
            }
        }
        for i in 1..r{
            for j in 1..c{
                if matrix[i][0]==0||matrix[0][j]==0{
                    matrix[i][j]=0;
                }
            }
        }
        if first_r{
            for j in 0..c{
                matrix[0][j]=0;
            }
        }
        if first_c{
            for i in 0..r{
                matrix[i][0]=0;
            }
        }
    }
}

//QED
//Problem 73 (Medium of Set Matrix Zeroes) - Jason Balayev (rust)