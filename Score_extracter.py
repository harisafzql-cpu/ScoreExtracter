with open("points.csv","r") as fhi:
    with open("grades.txt", "w") as fho:
        
        # header
        fho.write("Number A1 A2 A3 A4 A5 A6 A7 A8 Points Grade \n")

        # process each record
        for line in fhi:
            line = line.strip()
            parts = line.split(";")

            number = parts[0].strip()
            points = []

            for p in parts[1:]:
                points.append(float(p))

            total_points = sum(points)

            if total_points >= 72:
                grade = 1.0
            elif total_points >= 64:
                grade = 1.7
            elif total_points >= 56:
                grade = 2.3
            elif total_points >= 48:
                grade = 3.0
            elif total_points >= 40:
                grade = 4.0
            else:
                grade = 0.0

            # to output for the specific line
            fho.write(number + " ")
            for p in points:
                fho.write(f"{p:.1f} ")
            fho.write(f"{total_points:.1f} {grade:.1f} \n")
