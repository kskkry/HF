      program read_basisfunction
      implicit none
      integer :: i,j,k,num_bas,tmp
      double precision :: stndrd_const_val, orb_exp, tmp2
      character*128 :: f_path
      character*4 :: line
      character*2 :: element, orb

      read(*,*) f_path
      write(*,*) trim(f_path)
      open(99, file=trim(f_path), status='old')
      do 
       read(99,*) line
       write(*,'(A)') line(1:1) 

       if (line(1:1).ne."!".and.line(1:1).ne."/") then
        backspace(99)
        read(99,*) element, tmp
        write(*,'(A, I)') element, tmp
        exit
       endif
      enddo
      
      do  
       read(99,*) line
       write(*,*) line
       if (line(1:1).eq."*") then
        exit
       else
        backspace(99)
       endif

       read(99,*) orb, num_bas, tmp2
       write(*,*) orb, num_bas, tmp2
       do i=1, num_bas
        read(99,*) stndrd_const_val, orb_exp
       enddo
      enddo  
      

           

      write(*,'(A)') "exit"

      stop
      end

