# Rybka-Crafty Evidence III

Source: https://www.chessprogramming.org/Rybka-Crafty_Evidence_III

**[Home](/Main_Page "Main Page") \* [Organizations](/Organizations "Organizations") \* [ICGA](/ICGA "ICGA") \* [Investigations](/ICGA_Investigations "ICGA Investigations") \* [Rybka Controversy](/Rybka_Controversy "Rybka Controversy") \* [Pre-Fruit Rybka and Crafty](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty") \* Repeated zeroing of a Byte when clearing Pawn Hash**

**[< Prev](/Rybka-Crafty_Evidence_II "Rybka-Crafty Evidence II") [Next >](/Rybka-Crafty_Evidence_IV "Rybka-Crafty Evidence IV")**

by [Mark Watkins](/Mark_Watkins "Mark Watkins")

The [Crafty](/Crafty "Crafty") code varies over time, particularly with the data structure. The code appears in three places in Crafty, in init.c, in option.c, and in utility.c. The bug in question was fixed in init.c for 19.1 and in option.c for 19.16 (and never in utility.c until the nomenclature was re-done in 22.0). The pre-Beta Rybka executable also has three instances of such clearings, of which two contain the repeated zeroing of a specific byte. Note that the pre-Beta Rybka code has many distinctions from that of Crafty, not only in the byte-structure, but also in that not all structure fields are zeroed.

See also: [Why wouldn't the compiler remove the duplicate write?](https://icga.wikispaces.com/message/view/pre-fruit+Rybka+and+Crafty/35312878)

# Example Crafty code

(19.0 from option.c)

```
      pawn_hash_mask=(1<<log_pawn_hash)-1;
      for (i=0;i<pawn_hash_table_size;i++) {
        (pawn_hash_table+i)->key=0;
        (pawn_hash_table+i)->p_score=0;
        (pawn_hash_table+i)->protected=0;
        (pawn_hash_table+i)->black_defects_k=0;
        (pawn_hash_table+i)->black_defects_q=0;
        (pawn_hash_table+i)->white_defects_k=0;
        (pawn_hash_table+i)->white_defects_q=0;
        (pawn_hash_table+i)->passed_w=0;
        (pawn_hash_table+i)->passed_w=0;            // repeated zeroing
        (pawn_hash_table+i)->outside=0;
        (pawn_hash_table+i)->candidates_w=0;
        (pawn_hash_table+i)->candidates_b=0;
      }
```

# Code from pre-Beta Rybka executable

## First Instance

```
0x00446dc7:     xor    %ebx,%ebx               # set ebx to zero -- this will be stored everywhere
[...]
0x00446e6d:     mov    0x6b897c,%ecx           # load log_pawn_hash
0x00446e73:     mov    $0x1,%eax
0x00446e78:     shl    %cl,%eax                # (1 << log_pawn_hash)
0x00446e7a:     xor    %ecx,%ecx
0x00446e7c:     dec    %eax                    # subtract 1 from it
0x00446e7d:     mov    %eax,0x6b8994
0x00446e82:     cmp    %ebx,0x6b8990           # setup loop
0x00446e88:     jle    0x446ef8
0x00446e8a:     xor    %eax,%eax
0x00446e8c:     jmp    0x446ea0
0x00446e8e:     mov    0x6b8998,%edx
0x00446e94:     jmp    0x446ea0
0x00446e96:     lea    0x0(%esp),%esp
0x00446e9d:     lea    0x0(%ecx),%ecx
0x00446ea0:     mov    %ebx,(%eax,%edx,1)     # 4 bytes @ 0x0
0x00446ea3:     mov    0x6b8998,%edx
0x00446ea9:     mov    %ebx,0x4(%eax,%edx,1)  # 4 bytes @ 0x4 [might be part of 8-byte struct with above]
0x00446ead:     mov    0x6b8998,%edx
0x00446eb3:     mov    %bx,0x8(%eax,%edx,1)   # 2 bytes @ 0x8
0x00446eb8:     mov    0x6b8998,%edx
0x00446ebe:     mov    %bl,0xf(%eax,%edx,1)   # 1 byte @ 0xf
0x00446ec2:     mov    0x6b8998,%edx
0x00446ec8:     mov    %bl,0xf(%eax,%edx,1)   # repeated clearance of byte 0xf
0x00446ecc:     mov    0x6b8998,%edx
0x00446ed2:     mov    %bl,0xa(%eax,%edx,1)   # 1 byte @ 0xa
0x00446ed6:     mov    0x6b8998,%edx
0x00446edc:     mov    %bl,0x11(%eax,%edx,1)  # 1 byte @ 0x11
0x00446ee0:     mov    0x6b8998,%edx
0x00446ee6:     mov    %bl,0x10(%eax,%edx,1)  # 1 byte @ 0x10
0x00446eea:     mov    0x6b8990,%edx
0x00446ef0:     inc    %ecx
0x00446ef1:     add    $0x18,%eax             # struct has 24 bytes
0x00446ef4:     cmp    %edx,%ecx
0x00446ef6:     jl     0x446e8e
0x00446ef8:     pop    %ebx
0x00446ef9:     pop    %esi
0x00446efa:     ret    $0x4
0x00446efd:     int3
```

## Second Instance

```
0x00451fe5:     xor    %ecx,%ecx                  # ecx is zero, will set all bytes to this
[...]
0x004520e8:     xor    %eax,%eax                  # set up loop
0x004520ea:     lea    0x0(%ebx),%ebx
0x004520f0:     mov    0x6b8998,%esi
0x004520f6:     mov    %ecx,(%eax,%esi,1)         # 4 bytes @ 0x0
0x004520f9:     mov    0x6b8998,%esi
0x004520ff:     mov    %ecx,0x4(%eax,%esi,1)      # 4 bytes @ 0x4
0x00452103:     mov    0x6b8998,%esi
0x00452109:     mov    %cx,0x8(%eax,%esi,1)       # 2 bytes @ 0x8
0x0045210e:     mov    0x6b8998,%esi
0x00452114:     mov    %cl,0xf(%eax,%esi,1)       # 1 byte @ 0xf
0x00452118:     mov    0x6b8998,%esi
0x0045211e:     mov    %cl,0xe(%eax,%esi,1)       # 1 byte @ 0xe [not a repeat of 0xf]
0x00452122:     mov    0x6b8998,%esi
0x00452128:     mov    %cl,0xa(%eax,%esi,1)       # 1 byte @ 0xa
0x0045212c:     mov    0x6b8998,%esi
0x00452132:     mov    %cl,0x11(%eax,%esi,1)      # 1 byte @ 0x11
0x00452136:     mov    0x6b8998,%esi
0x0045213c:     mov    %cl,0x10(%eax,%esi,1)      # 1 byte @ 0x10
0x00452140:     mov    0x6b8990,%esi
0x00452146:     inc    %edx
0x00452147:     add    $0x18,%eax                 # struct has 24 bytes
0x0045214a:     cmp    %esi,%edx
0x0045214c:     jl     0x4520f0
0x0045214e:     pop    %esi
0x0045214f:     ret
```

Prior to this in the pre-Beta Rybka code there is a clearing of the general hash table, and similarly in Crafty's init.c there is a clearing of such a table preceding the pawn hash clearance. However, this pre-Beta Rybka has 24 byte entries in the general hash rather than the 16 bytes of Crafty, so there is some distinction.

## Third Instance

```
0x0045c8b5:     xor    %ecx,%ecx                       # ecx set to 0, will store in all bytes
[...]
0x0045c9a7:     xor    %eax,%eax
0x0045c9a9:     lea    0x0(%esp),%esp                  # loop start
0x0045c9b0:     mov    0x6b8998,%esi
0x0045c9b6:     mov    %ecx,(%eax,%esi,1)              # 4 bytes @ 0x0
0x0045c9b9:     mov    0x6b8998,%esi
0x0045c9bf:     mov    %ecx,0x4(%eax,%esi,1)           # 4 bytes @ 0x4
0x0045c9c3:     mov    0x6b8998,%esi
0x0045c9c9:     mov    %cx,0x8(%eax,%esi,1)            # 2 bytes @ 0x8
0x0045c9ce:     mov    0x6b8998,%esi
0x0045c9d4:     mov    %cl,0xf(%eax,%esi,1)            # 1 byte @ 0xf
0x0045c9d8:     mov    0x6b8998,%esi
0x0045c9de:     mov    %cl,0xf(%eax,%esi,1)            # 1 byte @ 0xf, repeating the previous
0x0045c9e2:     mov    0x6b8998,%esi
0x0045c9e8:     mov    %cl,0xa(%eax,%esi,1)            # 1 byte @ 0xa
0x0045c9ec:     mov    0x6b8998,%esi
0x0045c9f2:     mov    %cl,0x11(%eax,%esi,1)           # 1 byte @ 0x11
0x0045c9f6:     mov    0x6b8998,%esi
0x0045c9fc:     mov    %cl,0x10(%eax,%esi,1)           # 1 byte @ 0x10
0x0045ca00:     mov    0x6b8990,%esi
0x0045ca06:     inc    %edx
0x0045ca07:     add    $0x18,%eax                      # struct has 18 bytes
0x0045ca0a:     cmp    %esi,%edx
0x0045ca0c:     jl     0x45c9b0                        # END LOOP
0x0045ca0e:     mov    0x6b8d10,%eax                   # stores 0 in an 8-byte struct
0x0045ca13:     mov    %ecx,0xe28(%eax)                # possibly this corresponds
0x0045ca19:     mov    0x6b8d10,%edx                   # to "local[0]->pawn_score.key=0;"
0x0045ca1f:     mov    %ecx,0xe2c(%edx)                # in Crafty's utility.c
0x0045ca25:     pop    %esi                            
0x0045ca26:     ret
```

**[Up one level](/Pre-Fruit_Rybka_and_Crafty "Pre-Fruit Rybka and Crafty")**